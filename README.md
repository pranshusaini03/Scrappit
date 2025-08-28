# Scrappit

A Django 5 project for managing scrap pickup requests, customer reviews, and service inquiries.

## Features
- Pickup booking (`pickup` app)
- Service inquiries (`service` app)
- Customer reviews (`review` app)
- Static pages and pricing info

## Requirements
- Python 3.10+
- pip
- Virtual environment tool (venv)

## Setup (Windows PowerShell)
```powershell
# 1) Create and activate virtual environment
python -m venv .venv
. .venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run migrations
python manage.py migrate

# 4) (Optional) Create superuser to access admin
python manage.py createsuperuser

# 5) Start the development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Project Structure
- `Scrappit/` – project settings and URL routing
- `pickup/`, `service/`, `review/` – domain apps and models
- `templates/` – HTML templates for pages
- `static/` – CSS, images, and assets

## Configuration Notes
- Templates directory is configured at `BASE_DIR/templates`.
- Static files are served from `static/` in development; ensure `DEBUG=True`.
- Database defaults to SQLite (`db.sqlite3`). No extra DB setup required for local dev.

## Common Commands
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```

## License
This repository did not specify a license. Add one if you plan to distribute. 
