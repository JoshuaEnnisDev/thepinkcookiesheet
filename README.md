# Django Booking System with Tailwind CSS

A modern booking system built with Django and Tailwind CSS that allows customers to order products for specific dates.

## Features

- 📅 Date-based product booking system
- 👥 Customer information management
- 📦 Order tracking and management
- 🎨 Beautiful UI with Tailwind CSS
- 📱 Responsive design
- 🔐 Admin dashboard for managing bookings

## Tech Stack

- **Backend**: Django 5.0+
- **Frontend**: Tailwind CSS 3.x
- **Database**: SQLite (development) / PostgreSQL (production)
- **Python**: 3.10+

## Project Structure

```
booking_project/
├── manage.py
├── booking_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookings/
│   ├── migrations/
│   ├── templates/
│   │   └── bookings/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── booking_form.html
│   │       └── booking_success.html
│   ├── static/
│   │   └── css/
│   │       └── output.css
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── requirements.txt
├── tailwind.config.js
└── package.json
```

## Quick Start

### 1. Clone and Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Node Dependencies (for Tailwind)

```bash
npm install
```

### 4. Setup Database

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Build Tailwind CSS

```bash
npm run build:css
```

For development with auto-rebuild:
```bash
npm run watch:css
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the application.

## Database Models

### Customer
- First Name, Last Name
- Email (unique)
- Phone Number
- Address

### Product
- Name
- Description
- Price
- Available for booking

### Order
- Customer (ForeignKey)
- Product (ForeignKey)
- Booking Date
- Quantity
- Order Date
- Status (Pending, Confirmed, Completed, Cancelled)
- Special Instructions

## Admin Access

Access the admin panel at `http://localhost:8000/admin` to:
- View and manage customers
- Manage products
- Track orders and bookings
- Change order statuses

## Development Workflow

1. **Make model changes** in `bookings/models.py`
2. **Create migrations**: `python manage.py makemigrations`
3. **Apply migrations**: `python manage.py migrate`
4. **Update Tailwind styles** in templates (auto-compiled with watch)
5. **Test changes** in the browser

## Tailwind Configuration

Tailwind is configured to scan all Django templates and Python files for utility classes. Modify `tailwind.config.js` to customize:
- Colors
- Fonts
- Spacing
- Breakpoints

## Production Deployment

1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL database
4. Collect static files: `python manage.py collectstatic`
5. Build production CSS: `npm run build:css`
6. Use a production server (Gunicorn, uWSGI)

## Environment Variables

Create a `.env` file for sensitive data:
```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

## Contributing

1. Check `TASKS.md` for current todos
2. Create a feature branch
3. Make changes with clear commits
4. Test thoroughly
5. Submit a pull request

## License

MIT License - feel free to use for personal or commercial projects.