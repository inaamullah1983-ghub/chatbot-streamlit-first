import streamlit.web.cli as stcli
import os, sys

def resolve_path(path):
    # This helps the .exe find 'app.py' inside the bundled folder
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath("."), path)

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app.py"),
        "--server.fileWatcherType=none",  # Prevents the "Dictionary changed" error
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
