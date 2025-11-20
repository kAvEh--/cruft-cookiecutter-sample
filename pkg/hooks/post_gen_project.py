import os
import shutil
from pathlib import Path


def main():
    print("[post_gen] Starting hook...")
    project_dir = Path.cwd()
    template_root = Path(__file__).resolve().parent.parent
    source_common = template_root / "common"
    target_common = project_dir / "common"

    if source_common.is_dir():
        if not target_common.exists():
            shutil.copytree(source_common, target_common)
            print(f"[post_gen] Copied common -> {target_common}")
        else:
            print("[post_gen] common already exists; skipping copy.")
    else:
        print(f"[post_gen] Source common not found at {source_common}")

    # Create a marker file to assert hook execution
    marker = project_dir / ".post_gen_ran"
    marker.write_text("post_gen_project.py executed.\n")
    print(f"[post_gen] Marker file created at {marker}")


if __name__ == "__main__":
    main()
