# FigureForge

Django catalog of collectible figures, manufacturers, materials, reviews and requests.

## Local setup

1. Install Python compatible with the pinned Django version.
2. Create and activate a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Run `python manage.py migrate`.
5. Run `python manage.py runserver`.
6. Open http://127.0.0.1:8000/ and use the navigation to create manufacturers and materials before figures.

The default database is SQLite and does not require credentials. To use PostgreSQL, set `DB_ENGINE=postgresql` and supply `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` in your local `.env` file. 

## Features

Figure catalog with search and sorting; figure, manufacturer and material CRUD; reviews and requests; deletion confirmation and read-only figure fields on the deletion page.


