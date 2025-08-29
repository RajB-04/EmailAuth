# Email Domain Verifier

A full-stack Django application that verifies if an email domain is disposable or suspicious. This application helps protect your services from fake registrations and spam by identifying temporary email addresses.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-v4.2+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Features

- **🚀 Lightning Fast**: In-memory SQLite database for instant verification
- **📊 Comprehensive Database**: Extensive list of 500+ disposable email domains
- **🔍 Pattern Detection**: Identifies subdomain variations and patterns
- **📦 Bulk Processing**: Verify up to 100 emails in a single request
- **🎨 Modern UI**: Beautiful, responsive Bootstrap 5 interface
- **📱 Mobile Friendly**: Fully responsive design for all devices
- **🔗 RESTful API**: Easy integration with any application
- **📈 Statistics Dashboard**: View database statistics and sample domains
- **💾 Export Options**: Export bulk results to CSV or JSON

## Technology Stack

- **Backend**: Django 4.2+ with Python 3.8+
- **Database**: In-memory SQLite (as requested)
- **Frontend**: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript
- **Icons**: Font Awesome 6
- **API**: RESTful JSON API endpoints

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**:
   ```bash
   cd EmailAuth
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize and start the application**:
   ```bash
   python start_server.py
   ```
   
   This script will:
   - Apply database migrations
   - Populate the database with disposable domains
   - Start the development server

   **Alternative manual setup**:
   ```bash
   python manage.py migrate
   python manage.py populate_domains
   python manage.py runserver 8000
   ```

4. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000
   ```

The application uses SQLite database with 500+ disposable email domains pre-loaded.

## Usage

### Web Interface

1. **Single Email Verification**:
   - Enter an email address in the main form
   - Click "Verify Email" to check if it's disposable
   - View detailed results with domain information

2. **Bulk Email Verification**:
   - Enter multiple emails (one per line) in the bulk form
   - Click "Verify All Emails" to process up to 100 emails
   - Export results as CSV or JSON

3. **Statistics Page**:
   - View `/stats/` to see database statistics
   - Browse sample disposable domains
   - Check API endpoint information

### API Endpoints

#### Single Email Verification

```bash
POST /api/verify/
Content-Type: application/json

{
  "email": "user@tempmail.org"
}
```

**Response**:
```json
{
  "is_valid": true,
  "is_disposable": true,
  "is_suspicious": true,
  "message": "This email appears to be from a disposable/temporary email service",
  "domain": "tempmail.org",
  "email": "user@tempmail.org"
}
```

#### Bulk Email Verification

```bash
POST /api/bulk-verify/
Content-Type: application/json

{
  "emails": [
    "user1@gmail.com",
    "user2@tempmail.org",
    "user3@10minutemail.com"
  ]
}
```

**Response**:
```json
{
  "results": [
    {
      "email": "user1@gmail.com",
      "domain": "gmail.com",
      "is_valid": true,
      "is_disposable": false,
      "is_suspicious": false,
      "message": "Email domain appears to be legitimate"
    },
    {
      "email": "user2@tempmail.org",
      "domain": "tempmail.org",
      "is_valid": true,
      "is_disposable": true,
      "is_suspicious": true,
      "message": "This email appears to be from a disposable/temporary email service"
    }
  ],
  "total": 3,
  "disposable_count": 2,
  "suspicious_count": 2
}
```

## Project Structure

```
EmailAuth/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── emailauth/               # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── verifier/                # Email verification app
│   ├── __init__.py
│   ├── admin.py             # Django admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── views.py             # View functions and classes
│   ├── urls.py              # App URL configuration
│   └── utils.py             # Utility functions and domain list
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   └── verifier/            # App-specific templates
│       ├── index.html       # Main page
│       ├── stats.html       # Statistics page
│       └── about.html       # About page
└── static/                  # Static files
    ├── css/
    │   └── style.css        # Custom styles
    └── js/
        ├── main.js          # Common JavaScript
        └── email-verifier.js # Email verification logic
```

## Database

The application uses **SQLite database** for optimal performance and simplicity:

- ✅ **Fast Performance**: Lightweight SQLite database for instant access
- ✅ **Easy Setup**: No complex database configuration required
- ✅ **Auto-Population**: 500+ disposable domains loaded via management command
- ✅ **Persistent Data**: Database file persists between restarts

**For True In-Memory Database**: You can modify `settings.py` to use `:memory:` for the database name, but this requires special handling for migrations and data population.

The database contains 500+ common disposable email domains including:
- 10minutemail.com, tempmail.org, mailinator.com
- guerrillamail.com, yopmail.com, throwaway.email
- And many more temporary email services

## Customization

### Adding New Disposable Domains

Edit `verifier/utils.py` and add domains to the `get_common_disposable_domains()` function:

```python
def get_common_disposable_domains():
    return [
        # Add your domains here
        'your-disposable-domain.com',
        # ... existing domains
    ]
```

### Styling

Customize the appearance by editing `static/css/style.css`. The application uses CSS custom properties for easy theming:

```css
:root {
    --primary-color: #0d6efd;
    --success-color: #198754;
    --danger-color: #dc3545;
    /* ... other variables */
}
```

## API Integration Examples

### Python (requests)

```python
import requests

# Single email verification
response = requests.post('http://localhost:8000/api/verify/', 
                        json={'email': 'test@tempmail.org'})
result = response.json()
print(f"Is disposable: {result['is_disposable']}")

# Bulk verification
emails = ['user1@gmail.com', 'user2@tempmail.org']
response = requests.post('http://localhost:8000/api/bulk-verify/', 
                        json={'emails': emails})
results = response.json()
print(f"Verified {results['total']} emails")
```

### JavaScript (fetch)

```javascript
// Single email verification
const verifyEmail = async (email) => {
    const response = await fetch('/api/verify/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
    });
    return await response.json();
};

// Usage
const result = await verifyEmail('test@tempmail.org');
console.log('Is disposable:', result.is_disposable);
```

### cURL

```bash
# Single email verification
curl -X POST http://localhost:8000/api/verify/ \
     -H "Content-Type: application/json" \
     -d '{"email": "test@tempmail.org"}'

# Bulk verification
curl -X POST http://localhost:8000/api/bulk-verify/ \
     -H "Content-Type: application/json" \
     -d '{"emails": ["user1@gmail.com", "user2@tempmail.org"]}'
```

## Production Deployment

For production deployment, consider:

1. **Use a persistent database** (PostgreSQL, MySQL) instead of in-memory SQLite
2. **Configure static files** serving with whitenoise (included) or CDN
3. **Set environment variables** for security:
   ```bash
   export DJANGO_SECRET_KEY="your-secret-key"
   export DJANGO_DEBUG="False"
   export ALLOWED_HOSTS="yourdomain.com"
   ```
4. **Use gunicorn** (included in requirements):
   ```bash
   gunicorn emailauth.wsgi:application
   ```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed information
3. Include your Python and Django versions

## Acknowledgments

- Django framework for the robust backend
- Bootstrap for the beautiful UI components
- Font Awesome for the icons
- The open-source community for disposable domain lists

---

**Made with ❤️ using Django, HTML, CSS, and JavaScript** 