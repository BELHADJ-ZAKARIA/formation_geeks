Dealership Pro — Flask Inventory & Sales

Manage a car dealership’s inventory with CRUD, search, pagination, stats (Chart.js), and optional sales/customers/salespeople flows.
UI uses Tailwind CSS (CDN), charts use Chart.js (CDN). DB is PostgreSQL via psycopg2.

Table of Contents:
    > Requirements
    > Quickstart
    > Create & Activate a Virtual Environment (venv)
        >> Windows (PowerShell / cmd)
        >> macOS / Linux
    > Install Dependencies
    > Environment Variables
    > Database Setup (PostgreSQL)
    > Run the App

1 > Requirements:
    >> Python 3.10+
    >> PostgreSQL 13+ (local or remote)
    >> pip & venv


2 > Quickstart:
# 1) clone and cd
git clone <your-repo-url> dealership-pro
cd dealership-pro

# 2) create venv (choose the block for your OS below)
python -m venv .venv        # macOS/Linux
# or: py -3 -m venv .venv   # Windows

# 3) activate venv
source .venv/bin/activate   # macOS/Linux
# or: .\.venv\Scripts\Activate.ps1  # Windows PowerShell

# 4) install deps
python -m pip install --upgrade pip
pip install -r requirements.txt  # (or see Install Dependencies section)

# 5) configure env
cp .env.example .env  # if present; otherwise create .env from the snippet below

# 6) create db & seed
createdb dealership
psql -d dealership -f index.sql

# 7) run
python index.py
# open http://127.0.0.1:5000


3 > Create & Activate a Virtual Environment (venv):
A venv isolates Python packages per project.

3.1 >> Windows (PowerShell / cmd):
# Create
py -3 -m venv .venv

# Activate (PowerShell)
.\.venv\Scripts\Activate.ps1
# If you see a policy error:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Activate (cmd.exe)
.\.venv\Scripts\activate.bat


3.2 >> macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate


4 > Install Dependencies:
python -m pip install --upgrade pip
pip install -r requirements.txt


5 > Environment Variables:
Create a file named .env in the project root:
# Required for sessions/flash
SECRET_KEY=change-me-to-a-long-random-string

# Choose ONE style depending on database/index.py:

# A) DSN URL (common)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/dealership

# B) Separate vars
HOST=localhost
PORT=5001
DATABASE=dealership
USER=postgres
PASSWORD=postgres


6 > Database Setup (PostgreSQL):
Create the database and apply schema + seed:
# macOS/Linux
createdb dealership
psql -d dealership -f index.sql

# Windows (psql)
# createdb dealership (if available)
# psql -d dealership -f index.sql


7 > Run the App
Option A: Python: python index.py

Option B: Flask CLI
# PowerShell
$env:FLASK_APP = "index.py"; flask run
# cmd
set FLASK_APP=index.py && flask run
# macOS/Linux
export FLASK_APP=index.py
flask run