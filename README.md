# The Pink Cookie Sheet — Django scaffold

This repository includes a minimal Django project (`pinkcookies`) and a small app named `cookies`.

Quick start (Git Bash on Windows):

```bash
# create venv
python -m venv .venv
source .venv/Scripts/activate

# install dependencies
python -m pip install -r requirements.txt

# run migrations and start dev server
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the `cookies` app homepage.

Notes:
- The SECRET_KEY in `pinkcookies/settings.py` is a placeholder. Replace it for production.
- This scaffold is minimal — adjust settings, static handling, and deployment as needed.
