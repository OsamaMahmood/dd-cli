#!/bin/sh
# Legacy entry point. The actual implementation lives in the
# `dd-reimport-findings` console script installed by the defectdojo-cli
# package; this wrapper exists to preserve the file path that pre-v2
# CI pipelines invoke directly.
exec dd-reimport-findings "$@"
