Dealership Pro — Flask Inventory & Sales

A simple, clean Flask app for managing a car dealership’s inventory with CRUD, search, pagination, stats & charts, and optional sales + customers flows. Uses Tailwind CSS (CDN) for UI and PostgreSQL via psycopg2.

✨ Features
Inventory (Vehicles)

Create / Read / Update / Delete (CRUD)

Server-side validation + helpful flash messages

Pagination 6 items per page

Search by make/model

Online image support via photo_url

Database Design

Primary: vehicles

Secondary: customers, salespeople

Link (many-to-many): sales (vehicles ↔ customers, with salesperson_id)

Foreign keys with ON DELETE CASCADE

Seed data (≥ 10 vehicles, ≥ 10 customers, etc.)

Stats & Analytics

/stats dashboard

Aggregate queries (counts, grouping, average price)

Chart.js visualizations:

Vehicles by Make (bar)

Vehicles by Year (line)

Price Buckets (doughnut)

Average Price by Make (bar)

KPI cards: total vehicles, inventory value, most/least expensive

Optional flows (plug-and-play)

Sales: record a sale for a vehicle (customer + optional salesperson)

Customers: “Add customer” directly from the sale form; auto-preselect on return

🧱 Tech Stack

Backend: Python 3.10+ · Flask · Jinja2 · python-dotenv

DB: PostgreSQL · psycopg2

Frontend: Tailwind CSS (CDN) · Chart.js (CDN)

Runtime: Dev server (Flask). For production, use a WSGI server (gunicorn/uwsgi) + reverse proxy.

🗂 Project Structure (typical)
car_dealership_project/
├─ index.py                     # Flask app entry (registers blueprints, error handlers)
├─ models/
│  ├─ vehicles.py               # Inventory routes (CRUD, search, stats)
│  ├─ sales.py                  # (optional) Sales routes
│  └─ customers.py              # (optional) Customers routes
├─ database/
│  └─ index.py                  # get_db_connection() (uses env vars)
├─ templates/
│  ├─ base.html                 # Tailwind + navbar + flash renderer
│  ├─ index.html                # Inventory list + pagination
│  ├─ details.html              # Vehicle details (hero image)
│  ├─ create.html               # Add vehicle
│  ├─ edit.html                 # Edit vehicle
│  ├─ stats.html                # Chart.js dashboard
│  └─ sales/
│     ├─ index.html             # (optional) Sales listing
│     └─ new.html               # (optional) Record sale form
│  └─ customers/
│     └─ new.html               # (optional) Add customer form
├─ static/
│  └─ app.css                   # (optional) pure CSS alternative (if not using Tailwind)
├─ index.sql                    # Schema + seed data
├─ .env                         # Environment variables (SECRET_KEY, DB settings)
└─ README.md

✅ Prerequisites

Python 3.10+

PostgreSQL 13+ (running locally or remote)

pip + venv

🚀 Setup
1) Clone & create venv

git clone <this-repo-url> dealership-pro
cd dealership-pro
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

2) Install dependencies
If you have requirements.txt:

pip install -r requirements.txt

Else install minimal deps:

pip install flask python-dotenv psycopg2-binary

3) Configure environment

Create .env in the project root:

# Required for flash/session
SECRET_KEY=change-me-to-a-long-random-string

# One of the two styles below — pick what your database/index.py expects:

# DSN style (common)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/dealership

# Or discrete params (if your db helper uses them)
PGHOST=localhost
PGPORT=5432
PGDATABASE=dealership
PGUSER=postgres
PGPASSWORD=postgres

4) Create DB & seed

Create DB and run the schema/seed file:
# Create the database (psql or GUI)
createdb dealership  # or use psql: CREATE DATABASE dealership;

# Apply schema & sample data
psql -d dealership -f index.sql

If you added photo_url recently, ensure the column exists:
ALTER TABLE vehicles ADD COLUMN IF NOT EXISTS photo_url TEXT;

5) Run the app
uv run index.py

# Option : Flask CLI
set FLASK_APP=index.py        # Windows cmd
$env:FLASK_APP="index.py"     # PowerShell
export FLASK_APP=index.py     # macOS/Linux
flask run