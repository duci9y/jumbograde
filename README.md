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


## Templates

Templates common to more than one app go in the root `jinja2` folder.

Templates specific to apps must be placed according to the following directory
structure:

    <project_root>
    |   <app_name>
        |   jinja2
            |  <app_name>
               |   <template_name>.html.j2

Notice that `<app_name>` is repeated. This is because Jinja2 collates all
template files together in one 'virtual' directory. If you have a template
with the same name in two apps, they'll conflict. So, we namespace all
templates using their app's name. To use a template, you'll use the string
`app_name>/<template_name>.html.j2` to refer to it. An example is given in the
`urls.py` file of the `core` app. Just modify the template for `test_endpoint`
to whatever you create to test your templates, but please make sure you
restore it to `core/test.html.j2` before committing.

We only have one app right now, so it is okay for `layout.html.j2` to be the
only file in the root `jinja2` folder. Any templates you may create are most
likely going inside app-specific template directories.
