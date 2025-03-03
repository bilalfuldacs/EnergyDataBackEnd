# Energy Consumption API

A comprehensive Django REST Framework-based API for monitoring and analyzing energy consumption across various facilities and systems. This API provides real-time energy consumption data with standardized measurements and multi-system support.

## Features

### Core Functionality

- Real-time energy consumption monitoring
- Multi-facility data tracking
- Standardized measurement units
- Historical data analysis
- System-specific monitoring

### Supported Systems

- Building Management Systems
- Store Energy Systems
- Warehouse Energy Management
- Production Facility Monitoring

### Energy Forms Tracked

- Electricity (kWh)
- Heat (kWh)
- Cold (kWh)
- Gas (m³)
- Water (m³)

## Technology Stack

- **Backend Framework**: Django 4.2+
- **API Framework**: Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (recommended for production)
- **Authentication**: Django REST Framework authentication
- **CORS Support**: django-cors-headers

## Getting Started

### Prerequisites

1. Python 3.10+
2. Django 4.2+
3. Django REST Framework
4. Django CORS Headers

### Installation Steps

1. **Clone the Repository**

```bash
git clone <repository-url>
cd energy-backend
```

2. **Database Setup**

```bash
python manage.py migrate
```

3. **Run Development Server**

```bash
python manage.py runserver
```

## API Documentation

### Base URL

```
http://localhost:8000/api/
```

### Endpoints

#### 1. Energy Data Endpoint

- **URL**: `/api/energy-data/`
- **Method**: GET
- **Authentication**: Not required
- **Parameters**:
  - `system_type` (optional): Filter by system type
  - `energy_form` (optional): Filter by energy form
  - `start_date` (optional): Start date for data range
  - `end_date` (optional): End date for data range

**Example Request:**

```bash
GET /api/energy-data/
```

**Example Response:**

```json
{
  "status": "success",
  "data": [
    {
      "timestamp": "2025-03-01T00:00:00Z",
      "energyForm": "electricity",
      "systemType": "building A",
      "consumption": 1500,
      "unit": "kWh"
    }
  ]
}
```

## Project Structure

```
energy_backend/
├── energy_api/                 # Main API application
│   ├── migrations/            # Database migrations
│   ├── admin.py              # Admin interface configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Data models
│   ├── urls.py               # API URL routing
│   ├── views.py              # API view logic
│   └── tests.py              # Unit tests
├── energy_backend/           # Project configuration
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── requirements.txt          # Project dependencies
├── manage.py                # Django management script
└── README.md                # Project documentation
```
