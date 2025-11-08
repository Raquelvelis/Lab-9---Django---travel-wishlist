# Django Travel Wishlist

A simple Django web application to track places you want to visit and places you've already visited.

## Features

- Add places to your wishlist
- View list of places you want to visit
- Mark places as visited
- View separate list of places you've visited

## Installation

1. Clone this repository

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
cd wishlist
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000 in your browser

## Running Tests

```bash
cd wishlist
python manage.py test
```

All 7 unit tests should pass.

## Project Structure

```
django_wishlist/
├── venv/                          # Virtual environment (not in git)
├── wishlist/                      # Django project directory
│   ├── manage.py                  # Django management script
│   ├── db.sqlite3                 # Database (not in git)
│   ├── wishlist/                  # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   └── travel_wishlist/           # Main app
│       ├── models.py              # Place model
│       ├── views.py               # View functions
│       ├── forms.py               # NewPlaceForm
│       ├── urls.py                # URL patterns
│       ├── tests.py               # Unit tests
│       ├── admin.py               # Admin registration
│       ├── templates/             # HTML templates
│       │   └── travel_wishlist/
│       │       ├── base.html      # Base template
│       │       ├── wishlist.html  # Wishlist page
│       │       └── visited.html   # Visited page
│       ├── static/                # Static files
│       │   └── css/
│       │       └── style.css      # Custom styles
│       └── fixtures/              # Test data
│           └── test_places.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Usage

### Add a Place
1. Go to the home page
2. Enter place name in the form
3. Click "Add" button

### Mark as Visited
1. Find the place in your wishlist
2. Click the "Visited!" button next to it
3. The place moves to the Visited page

### View Visited Places
- Click "Visited" link in navigation

## Technologies

- Python
- Django
- SQLite
- HTML/CSS (with Sakura CSS framework)

## Student Project

This project demonstrates:
- Django models and ORM
- Django views and templates
- Template inheritance
- Forms and form processing
- Static files
- URL routing
- Unit testing with fixtures
# Lab-9---Django---travel-wishlist
