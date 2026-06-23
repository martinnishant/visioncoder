from pathlib import Path

WORKSPACE = Path("workspace")

def save_project(files):
    WORKSPACE.mkdir(exist_ok=True)

    for filename, content in files.items():
        file_path = WORKSPACE / filename
        file_path.write_text(content, encoding="utf-8")