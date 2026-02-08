# URL Shortener

A simple and clean URL shortener built with Django. Transform your long URLs into short, shareable links with an intuitive web interface.

## Features

- 🔗 **URL Shortening** - Convert long URLs into 6-character short codes
- 🎨 **Clean Web Interface** - Modern, responsive design that works on all devices
- 📋 **Copy to Clipboard** - One-click copying of shortened URLs
- 📈 **Click Tracking** - Automatic click counting for analytics
- 🕒 **Recent History** - Session-based history of recent URLs
- ✅ **URL Validation** - Server-side validation with proper error handling
- 🔌 **REST API** - JSON API for programmatic access

## Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd url_shortener
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser**
   ```
   http://127.0.0.1:8000
   ```

## Usage

### Web Interface

1. **Shorten a URL**: Enter your long URL in the input field and click "Shorten URL"
2. **Copy Short URL**: Click the "Copy" button to copy the shortened URL to clipboard  
3. **View History**: Recent URLs are automatically saved in your session
4. **Clear History**: Use the "Clear History" button to remove all saved URLs

### API Endpoints

#### Create Short URL
```http
POST /api/shorten/
Content-Type: application/json

{
  "original_url": "https://example.com/very/long/url"
}
```

**Response:**
```json
{
  "original_url": "https://example.com/very/long/url",
  "short_code": "abc123", 
  "short_url": "http://127.0.0.1:8000/abc123/",
  "created_at": "2026-02-07T10:30:00Z"
}
```

#### Access Short URL
```http
GET /{short_code}/
```
Redirects to the original URL and increments click count.

## Tech Stack

- **Backend**: Django 6.0+
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development)
- **API**: Django REST Framework

<!-- ## Project Structure

```
url_shortener/
├── core/                   # Main application
│   ├── models.py          # UrlMapping model
│   ├── views.py           # Web views and API endpoints
│   ├── forms.py           # Django forms
│   ├── serializers.py     # DRF serializers
│   ├── templates/         # HTML templates
│   └── static/           # CSS stylesheets
├── url_shortener/         # Django project settings
├── manage.py             # Django management script
└── db.sqlite3           # SQLite database
``` -->

### Admin Interface
Access the Django admin at `http://127.0.0.1:8000/admin/` to manage URLs directly.