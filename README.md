<div align="center">FigureForge
Collectible Figures Management System
A Django web application for managing collectible figures, manufacturers, materials, reviews, and customer requests.

Django · Python · PostgreSQL · Django Templates · HTML & CSS

Getting Started · Features · All Routes · Database Setup
</div>About the Project
FigureForge is a server-rendered catalog and management application created as an individual Django Basics project. Visitors can browse figures, search and sort records, view details, and use forms to create, edit, or delete entries.

The user application handles customer requests; it does not implement account registration, login, or authentication.
Features
- Full create, read, update, and delete (CRUD) views for figures, manufacturers, materials, reviews, and requests.
- Search, sorting, and pagination on list pages.
- Related data: figures belong to manufacturers and can use multiple materials.
- Form validation and confirmation pages before deletion.
- Reusable Django templates, template inheritance, and custom template filters/tags.
- Custom 404 page.
- PostgreSQL database configured through environment variables.
Project Structure
figureForge/
├── common/              # Homepage and 404 handler
├── figures/             # Figure catalog and CRUD
├── manufacturers/       # Manufacturer CRUD
├── materials/           # Material CRUD
├── reviews/             # Review CRUD
├── user/                # Customer request CRUD (not authentication)
├── figureForge/          # Project settings and main URL configuration
├── templates/            # Shared and application templates
├── static/               # CSS, images, and other static assets
├── manage.py
├── requirements.txt
└── README.md
Getting Started
Prerequisites
- Python compatible with the Django version in requirements.txt
- PostgreSQL installed and running
- Git (for cloning the repository)
1. Clone the project
git clone YOUR_REPOSITORY_URL
cd figureForge
Replace YOUR_REPOSITORY_URL with the actual public GitHub URL. Run the following commands from the folder containing manage.py.
2. Create a virtual environment
Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
python -m pip install -r requirements.txt
[!IMPORTANT]
In the supplied project archive, requirements.txt is saved as UTF-16. Convert it to UTF-8 before running this command or publishing the repository. The listed dependencies include Django, psycopg2, and python-decouple.

PostgreSQL Configuration
4. Create the database and database user
Connect to PostgreSQL as an administrator (for example, using psql) and run:
CREATE USER figureforge_user WITH PASSWORD 'choose_a_strong_password';
CREATE DATABASE figureforge_db OWNER figureforge_user;
The names above are examples; they must match the environment settings below.
5. Configure environment variables
Create a .env file next to manage.py:
DB_NAME=figureforge_db
DB_USER=figureforge_user
DB_PASSWORD=choose_a_strong_password
DB_HOST=127.0.0.1
DB_PORT=5432
These five variables are required by figureForge/settings.py, which uses python-decouple and the django.db.backends.postgresql engine. This project uses PostgreSQL, not SQLite.
[!CAUTION]
Never commit .env or real passwords to GitHub. The uploaded version also has a development SECRET_KEY and DEBUG=True in settings.py; these settings are not suitable for public production deployment.

6. Apply migrations and start the server
python manage.py check
python manage.py migrate
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.
URL Routes
Local base URL: http://127.0.0.1:8000

These are HTML page routes, not REST API endpoints. GET displays pages and forms. POST submits create/update forms or confirms deletion. Replace {id} with the database ID of an existing object, such as 1.
Home and administration
Method	URL	Django name	Description
GET	/	common:home-page	Homepage with recent figures and summary information.
GET / POST	/admin/	Django admin	Built-in Django administration (not required to manage project records).


Figures
Method	URL	Django name	Description
GET	/figures/	figures:list	Browse, search, sort, and paginate figures.
GET / POST	/figures/add/	figures:add	Display the form and create a figure.
GET	/figures/{id}/	figures:detail	View one figure and its details.
GET / POST	/figures/{id}/update/	figures:edit	Edit an existing figure.
GET / POST	/figures/{id}/delete/	figures:delete	Confirm and delete a figure.


Search: title, character_name
Sort options: title, -title, base_price, -base_price, -pk

Example: /figures/?q=naruto&sort=base_price
Manufacturers
Method	URL	Django name	Description
GET	/manufacturers/	manufacturers:list	Browse, search, sort, and paginate manufacturers.
GET / POST	/manufacturers/add/	manufacturers:add	Create a manufacturer.
GET	/manufacturers/{id}/	manufacturers:detail	View manufacturer details.
GET / POST	/manufacturers/{id}/update/	manufacturers:edit	Edit a manufacturer.
GET / POST	/manufacturers/{id}/delete/	manufacturers:delete	Confirm and delete a manufacturer.


Search: name
Sort options: name, -name

Example: /manufacturers/?q=bandai&sort=name
Materials
Method	URL	Django name	Description
GET	/materials/	materials:list	Browse, search, sort, and paginate materials.
GET / POST	/materials/add/	materials:add	Create a material.
GET	/materials/{id}/	materials:detail	View material details.
GET / POST	/materials/{id}/update/	materials:edit	Edit a material.
GET / POST	/materials/{id}/delete/	materials:delete	Confirm and delete a material.


Search: name
Sort options: name, -name

Example: /materials/?q=resin&sort=-name
Reviews
Method	URL	Django name	Description
GET	/reviews/	reviews:list	Browse, search, sort, and paginate reviews.
GET / POST	/reviews/add/	reviews:add	Create a review.
GET	/reviews/{id}/	reviews:detail	View review details.
GET / POST	/reviews/{id}/edit/	reviews:edit	Edit a review.
GET / POST	/reviews/{id}/delete/	reviews:delete	Confirm and delete a review.


Search: author_name, comment
Sort options: pk, -pk

Example: /reviews/?q=great&sort=-pk
Customer Requests
Method	URL	Django name	Description
GET	/requests/	user:list	Browse, search, sort, and paginate customer requests.
GET / POST	/requests/add/	user:add	Create a customer request.
GET	/requests/{id}/	user:detail	View request details.
GET / POST	/requests/{id}/edit/	user:edit	Edit a customer request.
GET / POST	/requests/{id}/delete/	user:delete	Confirm and delete a request.


Search: name
Sort options: pk, -pk

Example: /requests/?q=alex&sort=-pk
Custom 404 Error Page
Unrecognized URLs (for example, /not-found/) return HTTP 404 and display the project's 404.html through common.views.page_not_found.

To test the custom page locally, temporarily set DEBUG=False and include 127.0.0.1 and localhost in ALLOWED_HOSTS. With DEBUG=True, Django normally displays its development 404 page.
Search, Sorting and Pagination
List pages accept these optional query parameters:
Parameter	Purpose	Example
q	Case-insensitive search in the app's supported fields	?q=naruto
sort	Sort using one of the allowed fields; - means descending	?sort=-base_price
page	Select a results page (12 items per page)	?page=2


Parameters can be combined: /figures/?q=naruto&sort=-base_price&page=1.
First-Time Usage
Starting with an empty PostgreSQL database:
1. Visit /manufacturers/add/ and create a manufacturer.
2. Visit /materials/add/ and create at least one material.
3. Visit /figures/add/ and create a figure, selecting its manufacturer and materials.
4. Open /figures/ to browse figures, then open a detail page to edit or delete a record.
5. Visit /reviews/add/ to create a review.
6. Visit /requests/add/ to create a customer request.
7. Try searching, sorting, and pagination on the list pages.
Records should be created through the application's interface rather than preloaded fixtures or Django Admin.
Development Checks
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
Note: The routes in this document were checked against the supplied figureForge(9).zip source files. This README is documentation, not proof that every CRUD workflow has passed a live runtime test.
GitHub Submission Notes
- Keep .env, .venv/, __pycache__/, local databases, and secrets out of Git.
- Publish a public repository and submit its actual URL.
- Check that the repository has at least five commits on five separate days, as required by the assignment.
- Verify the project starts with an empty database after installing dependencies and applying migrations.
<div align="center">FigureForge · Django Basics Individual Project
</div>