![](./app/home/static/home/img/logo.png)

# [Great Commissioners International](https://github.com/tawalabora/gci)

## Environment Variables

During development, the `.env` file is optional as the system will use default values as `DEBUG`  settings will be **`True`**. However, if you need to customize any settings, copy these variables into your `.env` and update the values as needed.

```bash
# -------------- Debug setting --------------
# The default is 'True' unless explicitly changed in settings.py
# Ensure DEBUG is 'False' when in production.

DEBUG="False"

# -------------- Secret key setting --------------
# The default is 'Make sure to set your own secret key!'

SECRET_KEY="vdfasW^f34rewdfK3io2r230dbicndori329!3obsx"

# -------------- Allowed hosts setting --------------
# The default is 'localhost,127.0.0.1,dev.treeolive.tech'.
# Ensure you still include 'localhost' and '127.0.0.1' as well, together with your site domain
# when in production.

ALLOWED_HOSTS="localhost,127.0.0.1,example.com,www.example.com"

# -------------- Database settings --------------
# When DEBUG is 'True' it uses a sqlite database with a file named `db.sqlite3`.
# The below settings only apply when DEBUG is 'False' unless explicitly changed in `settings.py`.

DB_ENGINE="django.db.backends.postgresql"
DB_USER=""
DB_PASSWORD=""
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME=""

# -------------- Email settings --------------
# When DEBUG is 'True' it uses the console as an email backend
# therefore any email sent is printed out in the console / terminal.
# The below settings only apply when DEBUG is 'False' unless explicitly changed in settings.py.

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_HOST="smtp.gmail.com"
```

## Poetry Setup

1. Install Poetry using pip.
```bash
pip install poetry
```

2. (Optional) Configure Poetry to create virtualenv in project directory.
```bash
poetry config virtualenvs.in-project true
```

3. Install project dependencies.
```bash
poetry install
```

This will create a virtual environment and install all dependencies specified in `pyproject.toml`.

## Database Setup

After installing dependencies, set up the database.

```bash
python manage.py makemigrations
python manage.py migrate
```

(Optional) If you want to populate the database with sample data, copy the contents `seed_example.json` fixtures file provided in a django app fixtures directory, and create a new json file with the copied contents for editing.

**NOTE**: All other files created in the `fixtures` directory are gitignored. Only the `seed_example.json` fixture file is tracked by Git, as it serves as a template for creating your own fixtures.

After creating your own fixtures, run the following command to install all of them at once.

```bash

# Installs every fixture in every app except fixtures named 'seed_example.json'
python manage.py seed
```

