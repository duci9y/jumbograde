# Jumbograde

## Installation

Make sure you have the latest version of `pip` installed. If you don't have
virtualenv installed:

    pip install virtualenv

You can store your virtualenvs wherever you want. I keep them in
`~/.virtualenv`.

    mkdir ~/.virtualenv
    cd ~/.virtualenv

Create a virtualenv for this project in the directory you created above:

    virtualenv jumbograde

Then, go to the root of the project. Activate your virtualenv:

    source ~/.virtualenv/jumbograde/bin/activate

Install all the requirements:

    pip install -r requirements.txt

You only need to do those steps once after you have cloned the repository
locally.

## Running

We run locally using a sqlite3 database. The file will be called `db.sqlite3`.
In production, we would be using a MySQL database provided by EECS IT.

To be able to run with full functionality, you need to perform an additional
step. These would have to be redone whenever our database schema changes.
Django would warn you about these in red text, so don't worry about tracking
those changes, just do the steps again whenever it happens.

    ./manage.py migrate

Another thing you have to do at this point (only for the very first time) is
create a superuser for your particular database file.

    ./manage.py createsuperuser

And you're set! To run a local development server:

    ./manage.py runserver
