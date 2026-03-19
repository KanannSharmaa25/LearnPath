import streamlit as st
from streamlit.web import cli as stcli
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your app
import app_new

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app_new.py", "--server.port=8501", "--server.address=0.0.0.0"]
    sys.exit(stcli.main())
