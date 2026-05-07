# Multi-stage Dockerfile for defectdojo-cli.
#
# Stage 1 (builder): builds and installs the package into a venv. Has the
# .git directory available so hatch-vcs can derive the version.
#
# Stage 2 (runtime): copies just the venv onto a slim base, runs as a
# non-root user. The legacy `dd-reimport-findings` and `dd-import-languages`
# console scripts are on PATH automatically (installed by the wheel).
# Existing CI pipelines that called `dd-reimport-findings.sh` keep working
# via the shell wrappers in /usr/local/dd-cli/bin/ which now `exec` the
# console script directly.

# ---- builder ------------------------------------------------------------- #
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /build

# Install git so hatch-vcs can compute the version from the tagged commit.
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

# Create a venv and install the package into it. Building from the full
# checkout (.git included) lets hatch-vcs derive the right version.
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY . /build/
RUN pip install --upgrade pip \
    && pip install /build/

# ---- runtime ------------------------------------------------------------- #
FROM python:3.12-slim AS runtime

ARG user=ddcli
ARG group=ddcli

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Non-root user (preserves /opt/venv ownership for the runtime user).
RUN groupadd -g 1000 -r ${group} \
    && useradd -u 1000 -r -g ${group} -d /home/${user} -m ${user}

COPY --from=builder /opt/venv /opt/venv

# Legacy shell wrappers — preserved for CI pipelines that invoke them by
# path. They now just exec the installed console scripts.
RUN install -d -o ${user} -g ${group} /usr/local/dd-cli/bin
COPY --chown=${user}:${group} bin/dd-reimport-findings.sh /usr/local/dd-cli/bin/dd-reimport-findings.sh
COPY --chown=${user}:${group} bin/dd-import-languages.sh  /usr/local/dd-cli/bin/dd-import-languages.sh
RUN chmod +x /usr/local/dd-cli/bin/*.sh
ENV PATH="/usr/local/dd-cli/bin:$PATH"

WORKDIR /work
USER ${user}

ENTRYPOINT ["dd"]
CMD ["--help"]
