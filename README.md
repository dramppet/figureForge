FigureForge
FigureForge is a Django web application for managing collectible figures, manufacturers, materials, reviews, and customer requests/orders. It uses server-rendered Django templates and PostgreSQL as its database.
Technologies
- Python and Django 6.1.3 (version pinned in the supplied requirements.txt)
- PostgreSQL with psycopg2
- python-decouple for database environment variables
- Django templates, class-based views, forms, and custom template tags
- HTML/CSS frontend
Project applications
App	Responsibility
common	Homepage and custom 404 error handler
figures	Collectible figure catalog and CRUD
manufacturers	Manufacturer records and CRUD
materials	Figure material records and CRUD
reviews	Ratings/reviews and CRUD
user	Customer requests/orders and CRUD; not Django authentication


The Figure model has a many-to-one relationship with Manufacturer and a many-to-many relationship with Material.
Installation with PostgreSQL
1. Prerequisites
Install Python, PostgreSQL, and Git. Ensure that PostgreSQL is running and that you know the credentials for a PostgreSQL role allowed to access the application database.
2. Download and prepare
Clone your public repository (replace the placeholder with your actual repository URL), then open the folder containing manage.py:
git clone <YOUR_PUBLIC_REPOSITORY_URL>
cd figureForge
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Note: The uploaded project's requirements.txt is encoded in UTF-16. Save it as UTF-8 before using pip install -r requirements.txt. The supplied dependency list includes Django==6.1.3, psycopg2==2.9.13, and python-decouple==3.8. If package installation fails, check your Python version and platform compatibility.
3. Create the PostgreSQL database
Using psql while connected as a PostgreSQL administrator, for example:
CREATE USER figureforge_user WITH PASSWORD 'replace_with_a_strong_local_password';
CREATE DATABASE figureforge_db OWNER figureforge_user;
These are example names and credentials; you may choose different ones. Do not commit real passwords to Git.
4. Configure .env
Create a file named .env in the same directory as manage.py:
DB_NAME=figureforge_db
DB_USER=figureforge_user
DB_PASSWORD=replace_with_a_strong_local_password
DB_HOST=127.0.0.1
DB_PORT=5432
The uploaded figureForge/settings.py reads exactly these five variables through python-decouple and uses django.db.backends.postgresql. PostgreSQL is required by the current configuration; the project does not fall back to SQLite. Keep .env private and excluded from Git. The current SECRET_KEY and DEBUG=True are defined directly in settings.py; these settings are intended for local development, not production.
5. Initialize and run
python manage.py check
python manage.py migrate
python manage.py runserver
Open http://127.0.0.1:8000/. Migrations create the database schema; the user must create the application's records through the web interface. The application should not depend on fixture data.
Web endpoints
Base URL: http://127.0.0.1:8000

These endpoints render HTML pages; they are not REST/JSON API endpoints. GET loads pages and forms. Creation and editing forms submit with POST. Deletion confirmation also submits with POST. Replace <id> with the integer primary key of an existing record (for example, 1).
Homepage and administration
Method	Endpoint	URL name	Purpose
GET	/	common:home-page	Homepage: latest six figures and summary counts for figures, manufacturers, and reviews
GET/POST	/admin/	Django admin	Django's built-in administration, if configured with suitable credentials; not required for normal project usage


Figures (figures)
Method	Endpoint	URL name	Purpose
GET	/figures/	figures:list	List, search, sort, and paginate figures
GET, POST	/figures/add/	figures:add	Display and submit the form to create a figure
GET	/figures/<id>/	figures:detail	Show one figure's details
GET, POST	/figures/<id>/update/	figures:edit	Display and submit the figure editing form
GET, POST	/figures/<id>/delete/	figures:delete	Display deletion confirmation; delete after POST confirmation


Figures can be searched by title or character_name with ?q=.... Supported sort values are title, -title, base_price, -base_price, and -pk. Example: /figures/?q=naruto&sort=base_price&page=1.
Manufacturers (manufacturers)
Method	Endpoint	URL name	Purpose
GET	/manufacturers/	manufacturers:list	List, search, sort, and paginate manufacturers
GET, POST	/manufacturers/add/	manufacturers:add	Create a manufacturer
GET	/manufacturers/<id>/	manufacturers:detail	View manufacturer details
GET, POST	/manufacturers/<id>/update/	manufacturers:edit	Edit a manufacturer
GET, POST	/manufacturers/<id>/delete/	manufacturers:delete	Confirm and delete a manufacturer


Search by name using ?q=.... Supported sort values: name, -name. Example: /manufacturers/?q=bandai&sort=name.
Materials (materials)
Method	Endpoint	URL name	Purpose
GET	/materials/	materials:list	List, search, sort, and paginate materials
GET, POST	/materials/add/	materials:add	Create a material
GET	/materials/<id>/	materials:detail	View material details
GET, POST	/materials/<id>/update/	materials:edit	Edit a material
GET, POST	/materials/<id>/delete/	materials:delete	Confirm and delete a material


Search by name using ?q=.... Supported sort values: name, -name. Example: /materials/?q=resin&sort=-name.
Reviews (reviews)
Method	Endpoint	URL name	Purpose
GET	/reviews/	reviews:list	List, search, sort, and paginate reviews
GET, POST	/reviews/add/	reviews:add	Create a review
GET	/reviews/<id>/	reviews:detail	View one review
GET, POST	/reviews/<id>/edit/	reviews:edit	Edit a review
GET, POST	/reviews/<id>/delete/	reviews:delete	Confirm and delete a review


Search by author_name or comment using ?q=.... Supported sort values: pk, -pk. Example: /reviews/?q=great&sort=-pk.
Requests / Orders (user)
Method	Endpoint	URL name	Purpose
GET	/requests/	user:list	List, search, sort, and paginate customer requests/orders
GET, POST	/requests/add/	user:add	Create a request/order
GET	/requests/<id>/	user:detail	View one request/order
GET, POST	/requests/<id>/edit/	user:edit	Edit a request/order
GET, POST	/requests/<id>/delete/	user:delete	Confirm and delete a request/order


Search by name using ?q=.... Supported sort values: pk, -pk. Example: /requests/?q=alex&sort=-pk.
Custom 404 page
Method	Endpoint	Purpose
GET	Any unmatched URL, e.g. /unknown-page/	Displays the custom 404.html through common.views.page_not_found, returning HTTP 404


The handler is registered as handler404 = 'common.views.page_not_found' in the main figureForge/urls.py. To test the custom 404 locally, temporarily set DEBUG=False and configure ALLOWED_HOSTS to include 127.0.0.1 and localhost. Restore development settings afterward.
Query parameters for list pages
Parameter	Meaning	Example
q	Case-insensitive search in the fields supported by the specific list	?q=naruto
sort	Sort by one of the allowed fields listed above; a leading - means descending	?sort=-base_price
page	Page number, with up to 12 records per page	?page=2


Unrecognized sort values are ignored by the current list views.
How to use the project from an empty database
1. Open /manufacturers/add/ and create a manufacturer.
2. Open /materials/add/ and create one or more materials.
3. Open /figures/add/ and create a figure, selecting the related manufacturer and materials.
4. Browse /figures/, open a detail page, and try updating a figure.
5. Use /reviews/add/ to create a review and /requests/add/ to create a customer request/order.
6. Test search, sorting, pagination, and deletion confirmation on the list and detail pages.
The application is intended to let the evaluator create records using its own UI rather than requiring Django Admin or preloaded fixtures.
Development checks
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py runserver
Also test each CRUD operation and the navigation links manually. These instructions document the routes found in the supplied FigureForge (9) source code; they do not claim that every route has passed an automated runtime test.
Repository and security notes
- Publish the project to a public GitHub repository and submit its actual URL.
- Keep .env, .venv/, __pycache__/, and local secrets out of the repository.
- Do not include real database passwords in documentation or screenshots.
- Verify the exam's Git history requirement (at least five commits on five different days).
- DEBUG=True and the hardcoded development secret key in the supplied settings must not be used in a production deployment.
- The project uses PostgreSQL as requested; do not replace the database backend with SQLite.