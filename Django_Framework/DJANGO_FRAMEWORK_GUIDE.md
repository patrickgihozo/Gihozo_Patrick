# How the Django Framework Works

This document explains how to create a Django project, what its files do, how the files work together, and where to put the code used to build a normal web application.

The examples use this repository's names:

- Project: `hello`
- Application: `main`
- Virtual environment: `.venv`

## 1. What Django Is

Django is a Python web framework. It provides ready-made tools for URLs, web pages, databases, forms, authentication, administration, security, and testing.

A Django website normally contains:

- One **project**, which holds settings for the whole website.
- One or more **apps**, which hold individual features of the website.

For example, a school system could have one project named `school_system` and apps named `students`, `teachers`, and `payments`.

## 2. How a Browser Request Moves Through Django

When a user visits a page, Django handles the request in this order:

```text
Browser request
      |
      v
Project urls.py
      |
      v
App urls.py (recommended for larger applications)
      |
      v
View in views.py
      |
      +----> Model in models.py ----> Database
      |
      v
HTML template
      |
      v
HTTP response returned to the browser
```

Example: a browser requests `/students/`. Django finds that path in `urls.py`, runs the connected view, the view can read student records through a model, and then the view sends those records to an HTML template.

## 3. Step-by-Step Commands to Create a Django Project

The following commands are for Windows PowerShell. Begin in the folder where you want the `Django_Framework` directory to be located.

### Step 1: Create and enter the main folder

```powershell
mkdir Django_Framework
cd Django_Framework
```

### Step 2: Create a virtual environment

```powershell
python -m venv .venv
```

A virtual environment keeps this project's packages separate from other Python projects.

### Step 3: Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run this command for the current terminal and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Django

```powershell
python -m pip install django
python -m django --version
```

### Step 5: Create the project

```powershell
django-admin startproject hello
cd hello
```

`manage.py` should now be in the current directory.

### Step 6: Create an app

```powershell
python manage.py startapp main
```

### Step 7: Register the app

Open `hello/settings.py` and add `main` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
]
```

This step tells Django to load the app's models, templates, migrations, administration configuration, and other app features.

### Step 8: Create the database tables

```powershell
python manage.py migrate
```

The default database is SQLite, stored in `db.sqlite3`.

### Step 9: Run the development server

```powershell
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in a browser. Stop the server with `Ctrl+C`.

## 4. Project Structure and Important Files

The recommended structure is:

```text
Django_Framework/
|-- .venv/                         Virtual environment (do not edit)
|-- DJANGO_FRAMEWORK_GUIDE.md      This guide
`-- hello/                         Project working directory
    |-- manage.py                  Django command runner
    |-- db.sqlite3                 Development database
    |-- hello/                     Project configuration package
    |   |-- __init__.py            Marks this directory as a Python package
    |   |-- settings.py            Whole-site settings
    |   |-- urls.py                Starting URL routes
    |   |-- asgi.py                Entry point for ASGI servers
    |   `-- wsgi.py                Entry point for WSGI servers
    `-- main/                      Application containing normal feature code
        |-- migrations/            Database change history
        |-- templates/
        |   `-- main/              App HTML templates
        |       `-- home.html
        |-- static/
        |   `-- main/              App CSS, JavaScript, and images
        |       |-- css/
        |       |-- js/
        |       `-- images/
        |-- __init__.py            Marks the app as a Python package
        |-- admin.py               Registers models in Django admin
        |-- apps.py                App configuration
        |-- forms.py               Forms (create this when needed)
        |-- models.py              Database table definitions
        |-- tests.py               Automated tests
        |-- urls.py                App URL routes (create this)
        `-- views.py               Request-handling logic
```

### `manage.py`

Runs commands for this project. Run it from the directory containing the file.

```powershell
python manage.py runserver
python manage.py migrate
python manage.py test
```

### Project `hello/settings.py`

Controls the entire site, including installed apps, database connection, middleware, templates, static files, language, time zone, and security settings.

Important settings include:

- `INSTALLED_APPS`: apps enabled in the project.
- `DATABASES`: database configuration.
- `TEMPLATES`: template engine configuration.
- `STATIC_URL`: URL used for static files.
- `DEBUG`: detailed errors during development; it must be `False` in production.
- `SECRET_KEY`: secret security value; never publish a production key.
- `ALLOWED_HOSTS`: domain names allowed to serve the site.

### Project `hello/urls.py`

This is the main URL map. A scalable project sends app-specific paths to each app's `urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
]
```

### App `main/urls.py`

Create this file to keep the `main` app's routes together:

```python
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
]
```

### App `main/views.py`

Views receive requests and return responses. A simple text response is:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")
```

A normal web page usually renders a template:

```python
from django.shortcuts import render


def home(request):
    context = {"page_title": "Home"}
    return render(request, "main/home.html", context)
```

### App `main/models.py`

Models describe data stored in database tables:

```python
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

After changing a model, create and apply a migration:

```powershell
python manage.py makemigrations
python manage.py migrate
```

### App `main/admin.py`

Register a model so that it can be managed through `/admin/`:

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

Create an administrator account:

```powershell
python manage.py createsuperuser
```

Run the server and visit `http://127.0.0.1:8000/admin/`.

### App `main/templates/main/home.html`

Templates contain the HTML shown in the browser:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ page_title }}</title>
</head>
<body>
    <h1>Welcome to Django</h1>
</body>
</html>
```

The repeated `main` directory in `templates/main/home.html` prevents filename conflicts when several apps have a `home.html` file.

### App `main/static/main/`

Put CSS, JavaScript, images, fonts, and other browser assets here. For example, create `main/static/main/css/style.css`, then load it in a template:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'main/css/style.css' %}">
```

### App `main/forms.py`

This file is not created by `startapp`, but it is the normal place for Django forms:

```python
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "completed"]
```

### App `main/migrations/`

Migration files record changes to database structure. Django generates them with `makemigrations`. Keep migrations in version control; do not normally edit them manually.

### `asgi.py` and `wsgi.py`

These files connect Django to production web servers. Beginners normally leave them unchanged. `ASGI` supports asynchronous features; `WSGI` is the traditional synchronous interface.

## 5. Where Normal Project Work Is Put

Most day-to-day work belongs inside an app such as `main`, not inside the project configuration directory `hello/hello`.

| Work | Normal location |
|---|---|
| Database tables | `main/models.py` |
| Request logic | `main/views.py` |
| App routes | `main/urls.py` |
| HTML pages | `main/templates/main/` |
| CSS | `main/static/main/css/` |
| JavaScript | `main/static/main/js/` |
| Images | `main/static/main/images/` |
| Forms | `main/forms.py` |
| Admin configuration | `main/admin.py` |
| Tests | `main/tests.py` or a `main/tests/` package |
| Whole-site configuration | `hello/settings.py` |
| Top-level routes | `hello/urls.py` |

As an application grows, create more apps based on features. For example, put student-related work in a `students` app and payment-related work in a `payments` app.

## 6. How the Files Work Together: Complete Example

Suppose the `Task` model shown above has been created.

1. The browser requests `/`.
2. `hello/urls.py` sends the request to `main/urls.py`.
3. `main/urls.py` matches the empty path and calls `views.home`.
4. `main/views.py` reads tasks using the `Task` model.
5. The view passes the tasks to `main/templates/main/home.html`.
6. Django renders the HTML and returns it to the browser.

`main/views.py`:

```python
from django.shortcuts import render
from .models import Task


def home(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "main/home.html", {"tasks": tasks})
```

`main/templates/main/home.html`:

```html
<h1>Tasks</h1>

{% for task in tasks %}
    <p>{{ task.title }} - {{ task.completed }}</p>
{% empty %}
    <p>No tasks have been created.</p>
{% endfor %}
```

## 7. Important Commands

Run these commands from `Django_Framework/hello`, where `manage.py` is located.

| Command | Purpose |
|---|---|
| `python manage.py runserver` | Start the development server |
| `python manage.py startapp app_name` | Create a new app |
| `python manage.py check` | Check the project for common problems |
| `python manage.py makemigrations` | Create database change files |
| `python manage.py migrate` | Apply database changes |
| `python manage.py showmigrations` | Show migration status |
| `python manage.py createsuperuser` | Create an admin user |
| `python manage.py shell` | Open a Django-aware Python shell |
| `python manage.py test` | Run automated tests |
| `python manage.py collectstatic` | Gather static files for production |
| `python manage.py help` | List available commands |

Package commands:

```powershell
python -m pip install django
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

The first `requirements.txt` command records the installed package versions. The second installs those versions on another computer or environment.

## 8. Recommended Development Order

For each new feature, a useful order is:

1. Decide what page or feature is required.
2. Add or update models in `models.py` if data must be saved.
3. Run `makemigrations` and `migrate` after model changes.
4. Create forms in `forms.py` if the user enters data.
5. Write the view logic in `views.py`.
6. Add the route in the app's `urls.py`.
7. Create the HTML template.
8. Add CSS, JavaScript, and images under `static/main/`.
9. Register models in `admin.py` when admin management is useful.
10. Add tests and run `python manage.py test`.

## 9. Common Beginner Mistakes

- Running `manage.py` commands from the wrong directory.
- Creating an app but forgetting to add it to `INSTALLED_APPS`.
- Changing a model but forgetting `makemigrations` and `migrate`.
- Adding a view but forgetting to add its URL route.
- Putting templates or static files in incorrectly named directories.
- Editing `db.sqlite3` directly instead of using models and migrations.
- Committing `.venv`, `__pycache__`, or secret production settings to Git.
- Using the development server as a production server.

## 10. Current Repository Notes

In this repository, `hello/hello/urls.py` currently imports `home` directly from `main.views`, and `main/views.py` returns `Hello, Django!`. This works for a small example.

For a normal growing project, use `include("main.urls")` as shown above. Also add `main` to `INSTALLED_APPS` in `hello/hello/settings.py`; the current settings file does not yet register it.

The existing `db.sqlite3` file is the SQLite database. Treat it as application data rather than a Python source file.
jango-admin startproject hello
cd hello
python manage.py startapp main  