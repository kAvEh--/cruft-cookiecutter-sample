import os
import shutil
from pathlib import Path

def main():
    project_dir = Path.cwd()
    # Adjust source path relative to template structure
    template_root = Path(__file__).resolve().parent.parent
    print(template_root)
    print(project_dir)
    source_common = template_root / "common"
    target_common = project_dir / "common"
    if source_common.is_dir() and not target_common.exists():
        shutil.copytree(source_common, target_common)

if __name__ == "__main__":
    main()