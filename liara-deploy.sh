#!/bin/bash
set -e

BASE_DIR="$(dirname "$0")"

# Generate requirements.txt (windows-specific packages are excluded)
poetry -C "$BASE_DIR" export --format requirements.txt --only main |
    grep -v -i win \
        >"${BASE_DIR}/resume_api/requirements.txt"

# Run `liara deploy`
npx liara deploy --path "${BASE_DIR}/resume_api"
