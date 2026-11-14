#FigureForge — Collectible Figures Management System

##Django web application | PostgreSQL | SoftUni Django Basics Retake Exam

FigureForge is a web application for managing collectible figures, manufacturers, materials, customer orders, and reviews. It provides a browsable catalog and forms for managing related data directly through the website.
---
Table of Contents
- Project Overview
- Features
- Technology Stack
- Project Structure
- Database Schema
- Installation
- Environment Variables
- Running the Application
- Web Endpoints
- Filtering, Sorting and Pagination
- Working with an Empty Database
- Validation and Error Handling
- Testing
- Future Improvements
Project Overview
The project organizes collectible figure information in a relational PostgreSQL database. Each figure belongs to a manufacturer and can be associated with multiple materials. Visitors can browse figures, submit reviews, and create orders using the website's forms.

The project is a server-rendered Django website, not a JSON REST API. Its endpoints return HTML pages and process submitted forms. Authentication and user accounts are not part of the intended exam scope.
Features
- Browse collectible figures and their details
- Create, view, update, and delete figures
- Manage manufacturers and materials
- Add, edit, and delete figure reviews
- Create and manage customer orders
- Search and sort catalog records
- Pagination (12 items per list page)
- Form validation and deletion confirmation pages
- Reusable Django templates and custom template functionality
- Custom 404 — Page Not Found page
- PostgreSQL persistence using Django ORM
Technology Stack
- Python
- Django — web framework, templates, forms, ORM, and class-based views
- PostgreSQL — relational database
- HTML / CSS — frontend presentation
- django-decouple / python-decouple — environment-based database configuration (from decouple import config)
- Git and GitHub — version control
Project Structure
figureForge/
├── common/                 # Homepage and custom 404 view
├── figures/                # Figure catalog and CRUD
├── manufacturers/          # Manufacturer CRUD
├── materials/              # Material CRUD
├── reviews/                # Review CRUD
├── user/                   # Customer orders (Client model)
├── figureForge/            # Project settings and root URL configuration
│   ├── settings.py
│   └── urls.py
├── templates/               # Base, shared and application templates
├── static/                  # Static assets
├── manage.py
├── requirements.txt
├── .env                     # Local only; do not commit
└── README.md
The six Django applications separate the project's responsibilities. The user app represents customer orders; it does not implement Django authentication.
Database Schema
Model	Important fields	Relationships
Manufacturer	name, country	One manufacturer can have many figures
Material	name (unique)	Many-to-many with figures
Figure	title, character_name, base_price, height, slug	Foreign key to manufacturer; many-to-many to materials
Review	author_name, rating, comment, created_at	Foreign key to figure
Client	name, email, status_order, created_at	Foreign keys to figure and selected material


Relationships
Manufacturer (1) ────── (many) Figure
Figure       (many) ─── (many) Material
Figure       (1) ────── (many) Review
Figure       (1) ────── (many) Client
Material     (1) ────── (many) Client
Deleting a manufacturer referenced by a figure is restricted by PROTECT. Deleting a figure cascades to its related reviews and client orders according to the model definitions.
Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
Replace the placeholders with your actual public repository URL and directory name. Run the remaining commands from the directory containing manage.py.
2. Create a virtual environment
python -m venv .venv
Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
Windows (Command Prompt):
.venv\Scripts\activate.bat
macOS / Linux:
source .venv/bin/activate
3. Install dependencies
python -m pip install -r requirements.txt
Ensure requirements.txt is saved as UTF-8. The uploaded project previously contained a UTF-16 version.

4. Create a PostgreSQL database
Install and start PostgreSQL. Connect as a PostgreSQL administrator and execute:
CREATE USER figureforge_user WITH PASSWORD 'replace_with_strong_password';
CREATE DATABASE figureforge_db OWNER figureforge_user;
The example credentials are for local setup only. Do not reuse the example password in production.
Environment Variables
Create a .env file next to manage.py:
DB_NAME=figureforge_db
DB_USER=figureforge_user
DB_PASSWORD=replace_with_strong_password
DB_HOST=127.0.0.1
DB_PORT=5432
The current figureForge/settings.py reads these five variables using decouple.config and connects to PostgreSQL via django.db.backends.postgresql.

Security: Do not commit .env, real credentials, .venv, or local database backups. The uploaded version currently hardcodes SECRET_KEY and enables DEBUG; these settings should be secured before production deployment. This README does not claim that SECRET_KEY and DEBUG are already read from .env.
Running the Application
Apply the migrations:
python manage.py migrate
Start the local development server:
python manage.py runserver
Open the website:
http://127.0.0.1:8000/
Django's standard development server uses port 8000 unless another port is specified.
Web Endpoints
Base URL: http://127.0.0.1:8000

These are HTML page routes, not REST JSON endpoints. GET displays pages or forms. POST submits create/update forms or confirms deletion. Replace <id> with an existing numeric database primary key, such as 1.
Homepage and Administration
Method	URL	Purpose
GET	/	Homepage with latest figures and record counts
GET	/admin/	Built-in Django admin login/interface (not required for project data entry)


Figures
Method	URL	Purpose
GET	/figures/	List figures; search, sort, and paginate
GET, POST	/figures/add/	Display form / create a figure
GET	/figures/<id>/	View a figure's details
GET, POST	/figures/<id>/update/	Display form / update the figure
GET, POST	/figures/<id>/delete/	Display confirmation / delete the figure


Manufacturers
Method	URL	Purpose
GET	/manufacturers/	List manufacturers
GET, POST	/manufacturers/add/	Display form / create a manufacturer
GET	/manufacturers/<id>/	View manufacturer details
GET, POST	/manufacturers/<id>/update/	Display form / update manufacturer
GET, POST	/manufacturers/<id>/delete/	Display confirmation / delete manufacturer


Materials
Method	URL	Purpose
GET	/materials/	List materials
GET, POST	/materials/add/	Display form / create a material
GET	/materials/<id>/	View material details
GET, POST	/materials/<id>/update/	Display form / update material
GET, POST	/materials/<id>/delete/	Display confirmation / delete material


Reviews
Method	URL	Purpose
GET	/reviews/	List reviews
GET, POST	/reviews/add/	Display form / create a review
GET	/reviews/<id>/	View review details
GET, POST	/reviews/<id>/edit/	Display form / update review
GET, POST	/reviews/<id>/delete/	Display confirmation / delete review


Customer Orders
The URLs use /requests/ while the Django app is named user and the database model is named Client.
Method	URL	Purpose
GET	/requests/	List customer orders
GET, POST	/requests/add/	Display form / create an order
GET	/requests/<id>/	View order details
GET, POST	/requests/<id>/edit/	Display form / update order
GET, POST	/requests/<id>/delete/	Display confirmation / delete order


Custom 404 Page
An unmatched URL, such as /does-not-exist/, returns the custom 404.html template with HTTP status 404 when Django's production-style error handling is active (DEBUG=False). The root URL configuration registers handler404 = 'common.views.page_not_found'.
Filtering, Sorting and Pagination
List views accept URL query parameters. These parameters do not create additional Django URL routes.
Page	Search parameter	Allowed sort values
Figures	q — title or character name	title, -title, base_price, -base_price, -pk
Manufacturers	q — name	Check the manufacturer list view for supported sorting
Materials	q — material name	name, -name
Reviews	q — author name or comment	pk, -pk
Orders	q — customer name	pk, -pk


Examples:
/figures/?q=naruto
/figures/?sort=base_price
/figures/?sort=-base_price
/figures/?page=2
/materials/?q=resin
/reviews/?sort=-pk
/requests/?q=alex
The list views use paginate_by = 12. The page parameter selects a result page.
Working with an Empty Database
No prepopulated data should be required. After migrations, use the website's navigation and forms in this order:
1. Open /manufacturers/add/ and create a manufacturer.
2. Open /materials/add/ and create one or more materials.
3. Open /figures/add/ and create a figure using the existing manufacturer and materials.
4. Open /reviews/add/ to review an existing figure.
5. Open /requests/add/ to create a customer order for a figure and material.
6. Visit the list pages to inspect, edit, and delete records.
This order matters because figures reference manufacturers/materials, and reviews/orders reference existing figures.
Validation and Error Handling
- Figure price must be at least 0.01.
- Figure height must be at least 5.
- Figure slugs are unique.
- Material names are unique.
- Review ratings are limited to values from 1 to 5.
- Customer email addresses must be valid and unique.
- Deletion views present a confirmation page before a POST request removes an object.
- Nonexistent routes are handled by the custom 404 view when DEBUG=False.
Additional form-specific checks and messages are defined in each application's forms.py.
Testing
Run Django's configuration checks:
python manage.py check
Check whether model changes need migrations:
python manage.py makemigrations --check --dry-run
Run Django tests (if test cases are implemented):
python manage.py test
Manual verification checklist: create, inspect, update, and delete a record for each model; test invalid form input; test sorting and pagination; and open a nonexistent URL with DEBUG=False and a suitable ALLOWED_HOSTS setting.
The commands and routes above were documented from the uploaded project source. They are not a claim that all migrations and browser flows have already passed a live test.

Future Improvements
- Add automated tests for forms, views, and model relationships
- Improve validation messages and deletion handling for protected records
- Add more advanced figure filters
- Improve catalog image handling and responsive layouts
- Move deployment-sensitive settings to environment variables
- Add deployment documentation and automated CI checks
Author and Academic Context
FigureForge — Django Basics Retake Exam individual project, SoftUni (2026).

The project is intended to demonstrate Django models, relational database design, forms, class-based views, template inheritance, navigation, validation, and CRUD operations.
