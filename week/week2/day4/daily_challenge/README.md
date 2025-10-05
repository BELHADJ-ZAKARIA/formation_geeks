**10 Random Countries Using REST Countries API** 

## 🧪 Create & Activate a Virtual Environment (venv)

A **venv** isolates Python packages per project.

### Windows (PowerShell / cmd)

```powershell
# Create
uv venv .venv

# Activate (PowerShell)
.\.venv\Scripts\Activate.ps1
# If you see a policy error for scripts:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Activate (cmd.exe)
.\.venv\Scriptsctivate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To **deactivate** later:
```bash
deactivate
```

---

## 📦 Install Dependencies

```bash
uv pip install --upgrade pip
uv pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a **`.env`** file in the project root.

**Database config:**

**Generic style (if your code uses these):**
```env
HOST=localhost
PORT=5432
DATABASE=countries
USER=postgres
PASSWORD=postgres
```

## 🗄 Database Setup (PostgreSQL)

```bash
# macOS/Linux
createdb countries
psql -d countries -f countries.sql

# Windows (psql)
createdb countries  #(if available)
psql -d countries -f countries.sql
```

## Run the App

uv run .\countries.py