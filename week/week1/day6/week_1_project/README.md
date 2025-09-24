# Flask crud backend

## 1. setup the venv and install the dependencies using uv

using uv:

- uv sync
- uv run main.py

or using python and pip:

- python -m venv venv
- source venv/bin/activate (on mac or linux) or venv/Scripts/activate (on windows)
- pip install -r requirements.txt

## 2. run the app

- uv run main.py (dont need to activate the venv first)
- or
- python main.py (activate the venv first)

## 3. test the api

- install insomnia or postman (recommended)
- or thunder client extension in vscode
- or rest client extension in vscode (to use the test-api.rest file)