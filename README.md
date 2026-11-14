# FigureForge

Django catalog of collectible figures, manufacturers, materials, reviews and requests.

## Local setup

1. Create a virtual environment: `python -m venv .venv`
2. Activate it (Windows PowerShell): `.\.venv\Scripts\Activate.ps1`
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`
6. Open http://127.0.0.1:8000/.

No environment variables are required for local testing. For a custom secret key, copy `.env.example` to `.env` and set `SECRET_KEY`. Never commit `.env` or production credentials.

## Usage

Create a manufacturer and at least one material through the navigation, then add figures. Reviews and requests can also be created from the navigation. Lists provide searching and sorting; detail, edit and delete pages are accessible from each record. Deletion requires confirmation.

## Structure

- `common`: home page and custom 404 handler
- `figures`: collectible figure catalog and CRUD
- `manufacturers`: figure manufacturers and CRUD
- `materials`: available materials and CRUD
- `reviews`: ratings and comments
- `user`: customer requests (not authentication)

Figure has a many-to-one relationship with Manufacturer and a many-to-many relationship with Material.

## Important

The default configuration is for local development (`DEBUG=True`), not production deployment.


