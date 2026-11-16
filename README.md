# FigureForge — Figure Collection & Custom Requests

## Project Overview

FigureForge is a **Django web application** for managing a collectible figure catalog, manufacturers, materials, customer reviews, and custom figure requests.

Visitors can browse figures, search and sort the catalog, inspect figure details, and use web forms to create, edit, or delete records. Each figure belongs to a manufacturer and can be associated with multiple materials. Customers can submit requests for a figure and a selected material.

The application uses **Django's ORM**, server-rendered templates, and a **PostgreSQL** database. It was developed as an individual project for the **SoftUni Django Basics** course. Authentication and user accounts are not part of the project requirements.

---

# Features

* Web application built with **Django**
* Full **CRUD operations** for figures, manufacturers, materials, reviews, and customer requests
* Figure catalog with **search, sorting, and pagination**
* Figure details with price, height, manufacturer, and materials
* **One-to-many** relationship between manufacturers and figures
* **Many-to-many** relationship between figures and materials
* Customer reviews with **1–5 star ratings**
* Customer requests with figure and material selection
* **Django ModelForms** and model-level validation
* Reusable templates and responsive styling
* Custom **404 error page**
* **PostgreSQL** database integration

---

# Technology Stack

* Python
* Django 6.1.3
* PostgreSQL
* Django ORM
* Django Templates (HTML)
* CSS
* psycopg2
* python-decouple

---

# Project Structure

```text
figureForge/
│
├── common/
│   ├── templatetags/
│   ├── urls.py
│   └── views.py
│
├── figures/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manufacturers/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── materials/
│   ├── choices.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── reviews/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── user/                  # Customer requests (not authentication)
│   ├── choices.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── figureForge/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── common/
│   ├── figures/
│   ├── manufacturers/
│   ├── materials/
│   ├── reviews/
│   ├── user/
│   ├── shared/
│   ├── 404.html
│   └── base.html
│
├── static/
│   ├── css/
│   └── images/
│
├── manage.py
├── requirements.txt
└── README.md
```

Each data-management app also contains Django migrations and test modules.

---

# Database Schema (Relationships)

The database contains five main application models:

* **Manufacturer** — name, country
* **Material** — unique name
* **Figure** — title, character name, base price, height, unique slug, manufacturer, materials
* **Review** — author name, rating, comment, creation date, figure
* **Client** — name, unique email, order status, figure, chosen material, creation date

```text
Manufacturer (1) ──────── (N) Figure
                                 │
Material (N) ──────────── (N) ───┤
                                 │
Figure (1) ─────────────── (N) Review
                                 
Figure (1) ─────────────── (N) Client
Material (1) ──────────── (N) Client
```

Django manages the join table for the many-to-many relationship between figures and materials.

---

# Installation

Clone the repository (replace the URL with the actual GitHub repository URL):

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```powershell
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a PostgreSQL database and configure the environment variables below.

Apply migrations:

```bash
python manage.py migrate
```

---

# Environment Variables

Create a `.env` file in the project root, alongside `manage.py`.

Example:

```dotenv
DB_NAME=figureforge_db
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

The database settings in `figureForge/settings.py` read these values using **python-decouple**. Make sure PostgreSQL is running and the database already exists.

**Security:** Never commit `.env` or database credentials to GitHub. The supplied project currently contains a hardcoded Django `SECRET_KEY` in `settings.py`; move it to an environment variable before deploying or publishing a production-ready version.

---

# Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

The application uses regular Django HTML pages rather than a REST API or Swagger documentation.

---

# Figure Endpoints

List all figures:

```http
GET /figures/
```

Create a figure:

```http
GET  /figures/add/
POST /figures/add/
```

View figure details:

```http
GET /figures/{id}/
```

Update a figure:

```http
GET  /figures/{id}/update/
POST /figures/{id}/update/
```

Delete a figure:

```http
GET  /figures/{id}/delete/
POST /figures/{id}/delete/
```

The catalog view supports search and sorting through query parameters. For example:

```text
/figures/?q=batman
/figures/?sort=base_price
/figures/?sort=-base_price
```

---

# Manufacturer Endpoints

```http
GET  /manufacturers/
GET  /manufacturers/add/
POST /manufacturers/add/
GET  /manufacturers/{id}/
GET  /manufacturers/{id}/update/
POST /manufacturers/{id}/update/
GET  /manufacturers/{id}/delete/
POST /manufacturers/{id}/delete/
```

Each manufacturer has a name and country. A manufacturer referenced by a figure is protected from deletion through `on_delete=models.PROTECT`.

---

# Material Endpoints

```http
GET  /materials/
GET  /materials/add/
POST /materials/add/
GET  /materials/{id}/
GET  /materials/{id}/update/
POST /materials/{id}/update/
GET  /materials/{id}/delete/
POST /materials/{id}/delete/
```

Materials are stored as separate database records with unique names. A figure can use multiple materials.

---

# Review Endpoints

```http
GET  /reviews/
GET  /reviews/add/
POST /reviews/add/
GET  /reviews/{id}/
GET  /reviews/{id}/edit/
POST /reviews/{id}/edit/
GET  /reviews/{id}/delete/
POST /reviews/{id}/delete/
```

Each review belongs to a figure and contains an author, comment, and rating from **1 to 5**. Reviews are ordered by creation date, newest first.

---

# Customer Request Endpoints

```http
GET  /requests/
GET  /requests/add/
POST /requests/add/
GET  /requests/{id}/
GET  /requests/{id}/edit/
POST /requests/{id}/edit/
GET  /requests/{id}/delete/
POST /requests/{id}/delete/
```

A request links a customer name and email to a selected figure and material. The order status defaults to **Pending**. The `user` app manages customer requests; it does not implement login or registration.

---

# Home Page & Error Handling

Home page:

```http
GET /
```

The home page provides navigation to the catalog and other sections. A custom `handler404` renders the project's 404 page for unmatched URLs when Django is running with `DEBUG=False` and an appropriate host configuration.

---

# Data Validation

Django model fields and forms enforce validation rules, including:

* Figure price must be at least **0.01**
* Figure height must be at least **5 cm**
* Figure slug must be **unique** and is generated from the title and character name when missing
* Material name must be **unique**
* Review rating must be between **1 and 5**
* Customer email must be a valid email format and **unique**
* Customer request status uses predefined choices

---

# Testing

Run the Django test suite:

```bash
python manage.py test
```

The repository includes `tests.py` modules in its Django apps. Their presence does not imply comprehensive automated test coverage.

---

# Architectural Decisions

**Django Class-Based Views** are used to implement reusable list, detail, create, update, and delete workflows.

**Django ORM** manages database access and model relationships, avoiding manual SQL for normal application operations.

**PostgreSQL** is configured as the database backend through environment-based connection settings.

**ModelForms** provide form generation and validation based on the Django models.

**Reusable templates** keep the interface consistent across different catalog sections.

**No authentication** is implemented because the SoftUni Django Basics assignment excludes user management functionality.

---

# Future Improvements

* Add automated tests for all CRUD workflows and form validation
* Add a visual ER diagram and screenshots of the application
* Improve deployment configuration and secret management
* Add Docker and Docker Compose support
* Expand catalog filtering and sorting options
* Add CI checks for migrations and tests

---

# Author

**FigureForge**  
SoftUni — Django Basics Individual Project
