#!/usr/bin/env bash
set -euo pipefail

echo "[pre_gen] Starting"

# Expect: export ORIG_COMMON_PATH=/absolute/path/to/common before cruft create
echo $pwd

ls ../..

cp -R ../../common ./common
