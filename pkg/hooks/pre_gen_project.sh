#!/usr/bin/env bash
set -euo pipefail

echo "[pre_gen] Starting"

# Expect: export ORIG_COMMON_PATH=/absolute/path/to/common before cruft create
echo $pwd

SOURCE="${ORIG_COMMON_PATH:-}"
TARGET_DIR="common"  # Place alongside other template content

if [ -z "$SOURCE" ]; then
  echo "[pre_gen] ORIG_COMMON_PATH not set; skipping copy."
  exit 0
fi

if [ ! -d "$SOURCE" ]; then
  echo "[pre_gen] Source not found: $SOURCE"
  exit 0
fi

# Copy into template so it gets rendered
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"
cp -R "$SOURCE"/. "$TARGET_DIR"/

echo "[pre_gen] Copied common from $SOURCE -> $TARGET_DIR"
echo "[pre_gen] Done"
