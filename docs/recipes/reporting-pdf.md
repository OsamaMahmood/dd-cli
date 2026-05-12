# Reporting to PDF

`dd report generate` produces **Markdown and HTML**, not PDF. The rationale is install footprint: a built-in PDF renderer (WeasyPrint or similar) means `pango` / `cairo` / `gdk-pixbuf` as host dependencies, ~80 MB added to the Docker image, and a class of native-lib install failures we'd be on the hook to support. The HTML→PDF pipeline already lives on every machine that has a browser; reusing it keeps `pip install dd-cli` to a couple of pure-Python wheels.

Three paths below, in order of how often we expect people to reach for them.

## Path 1 — Browser print (zero install, best output)

This is what we recommend for one-off reports.

```bash
dd report generate --product 42 --format html
open ./reports/42-payments.html      # macOS
xdg-open ./reports/42-payments.html  # Linux
start ./reports/42-payments.html     # Windows
```

In the browser: ⌘P (macOS) / Ctrl+P → **"Save as PDF"**. The HTML template inlines all its CSS and uses print-friendly styles, so the output is essentially identical to what a dedicated HTML→PDF engine would produce.

Works on every browser. No dependencies, no flags, no surprises.

## Path 2 — `pandoc` (great for batch and CI)

For automated PDF generation in CI, `pandoc` is the most portable HTML/MD→PDF tool. It needs a LaTeX engine for PDF; `xelatex` is the typical pick.

```bash
# Markdown → PDF
pandoc reports/42-payments.md -o reports/42-payments.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in

# HTML → PDF (keeps the report's CSS-driven layout)
pandoc reports/42-payments.html -o reports/42-payments.pdf \
  --pdf-engine=weasyprint    # or wkhtmltopdf, or prince
```

Install:

```bash
brew install pandoc basictex                       # macOS
apt-get install pandoc texlive-xetex               # Debian/Ubuntu
```

For the HTML path, `pandoc` can shell out to whatever HTML→PDF engine is on `PATH`. If you have WeasyPrint installed at the system level (via your distro's package manager rather than `pip`), `--pdf-engine=weasyprint` gives you the same fidelity as a custom-built reporter without `dd-cli` taking the dependency.

### CI example

```yaml
# GitHub Actions — generate Markdown report and convert to PDF
- run: pip install dd-cli
- env:
    DD_URL: ${{ secrets.DD_URL }}
    DD_API_KEY: ${{ secrets.DD_API_KEY }}
  run: dd report generate --product 42 --format md --output-dir ./out

- run: |
    sudo apt-get update
    sudo apt-get install -y pandoc texlive-xetex
    pandoc ./out/42-payments.md -o ./out/42-payments.pdf \
      --pdf-engine=xelatex -V geometry:margin=1in

- uses: actions/upload-artifact@v4
  with:
    name: defectdojo-report
    path: ./out/42-payments.pdf
```

## Path 3 — Headless browser (faithful, heavier)

For pixel-faithful PDF identical to what a human would get from browser print, run a headless Chromium / Chrome. Works in CI; needs the browser binary on the host.

```bash
# Chromium / Chrome headless
chromium --headless --disable-gpu --no-sandbox \
  --print-to-pdf=./reports/42-payments.pdf \
  file://$PWD/reports/42-payments.html

# Or via Playwright (Python wrapper, batteries-included)
pip install playwright && playwright install chromium
python -c "
from playwright.sync_api import sync_playwright
import pathlib
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f'file://{pathlib.Path(\"reports/42-payments.html\").resolve()}')
    page.pdf(path='reports/42-payments.pdf', format='A4')
    browser.close()
"
```

Pick this if your CI already has Chromium (e.g. for E2E tests) — incremental cost is ~zero. If it doesn't, prefer Path 2 for smaller image churn.

## Path 4 — Standalone WeasyPrint (if your team already uses it)

If WeasyPrint is already installed system-wide (i.e. you have `pango` / `cairo` / `gdk-pixbuf` available), point it at the HTML:

```bash
pip install --user weasyprint                # or: pipx install weasyprint
weasyprint reports/42-payments.html reports/42-payments.pdf
```

This is the engine the original [`dd-reporting`](https://github.com/OsamaMahmood/dd-reporting) tool used internally. The output is excellent. The reason `dd-cli` doesn't depend on it: forcing every user to install native libs is a worse default than letting users opt in.

## Which one should I pick?

| Use case | Pick |
|---|---|
| One-off report for a meeting | **Path 1** — browser print |
| CI/CD pipeline generating PDFs nightly | **Path 2** — pandoc + `xelatex` |
| You need pixel-faithful output and your CI already has Chromium | **Path 3** — headless Chromium |
| Your team already uses WeasyPrint elsewhere | **Path 4** — standalone WeasyPrint |

If none of those fit, the HTML and Markdown files are still useful as-is — pipe them through `mdpdf`, `prince`, `wkhtmltopdf`, your wiki, your release notes, or whatever toolchain you already have.
