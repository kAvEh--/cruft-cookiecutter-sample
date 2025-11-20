import os
import shutil
import sys
from pathlib import Path

def log(msg: str) -> None:
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()

def main() -> None:
    # CWD is the rendered project root
    project_dir = Path.cwd()
    script_path = Path(__file__).resolve()
    # In rendered output: hooks/ is under project root
    rendered_root = script_path.parent.parent

    # If `common` was inside `pkg` it will now be directly under rendered_root.
    candidate_inside = rendered_root / "common"

    # If you used --directory=pkg and kept `common` as a sibling in the original repo,
    # it is NOT rendered. This fallback only works if cookiecutter left a copy (rare).
    # Attempt one more parent hop (defensive).
    candidate_outside = rendered_root.parent / "common"

    # Select first existing source
    for source_common in (candidate_inside, candidate_outside):
        if source_common.is_dir():
            break
    else:
        log("[post_gen] No source 'common' directory found. (Move 'common' inside 'pkg' to include it.)")
        (project_dir / ".post_gen_ran").write_text("post_gen ran; no common copied.\n")
        return

    target_common = project_dir / "common"
    if target_common.exists():
        log(f"[post_gen] Target already exists: {target_common} (skipping copy)")
    else:
        shutil.copytree(source_common, target_common)
        log(f"[post_gen] Copied common from {source_common} -> {target_common}")

    (project_dir / ".post_gen_ran").write_text("post_gen ran; common copied.\n")
    log("[post_gen] Marker file written (.post_gen_ran)")

if __name__ == "__main__":
    try:
        log("[post_gen] Starting hook...")
        main()
        log("[post_gen] Completed.")
    except Exception as e:
        log(f"[post_gen] ERROR: {e!r}")
        raise
