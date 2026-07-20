import os
import subprocess
import webbrowser
import time

def preview_project():
    workspace_path = os.path.abspath("workspace")

    server = subprocess.Popen(
        ["python", "-m", "http.server", "8000"],
        cwd=workspace_path
    )

    time.sleep(2)

    webbrowser.open("http://localhost:8000")

    return server
    