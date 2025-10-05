**Restaurant Menu Manager** 

## 🧪 Create & Activate a Virtual Environment (venv)

A **venv** isolates Python packages per project.

### Windows (PowerShell / cmd)

```powershell
# Create
py -3 -m venv .venv

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
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a **`.env`** file in the project root.

**Database config:**

**Generic style (if your code uses these):**
```env
HOST=localhost
PORT=5432
DATABASE=menu_rest
USER=postgres
PASSWORD=postgres
```

## 🗄 Database Setup (PostgreSQL)

```bash
# macOS/Linux
createdb menu_rest
psql -d menu_rest -f menu_rest.sql

# Windows (psql)
createdb menu_rest  #(if available)
psql -d menu_rest -f menu_rest.sql
```

## Run the App

uv run .\menu_editor.py