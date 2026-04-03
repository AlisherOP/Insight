# ⚡️ Insight AI - Document Analysis Engine

An asynchronous backend API built with **Django Rest Framework**, **Celery**, and **Redis** that extracts text from PDFs and provides AI-powered summaries and sentiment analysis.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14+-red.svg)](https://www.django-rest-framework.org/)
[![Celery](https://img.shields.io/badge/Celery-5.3+-37814A.svg)](https://docs.celeryq.dev/en/stable/)
[![Redis](https://img.shields.io/badge/Redis-7.x-DC382D.svg)](https://redis.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 Table of Contents
- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Application (Local Development)](#-running-the-application-local-development)
- [API Documentation](#-api-documentation)
- [Deployment (Production)](#-deployment-production)
- [License](#-license)

---

## 💡 About The Project

**Insight AI** is designed to process heavy document analysis tasks in the background without blocking your main API threads. By combining the robustness of Django with the asynchronous power of Celery and Redis, this API enables users to securely upload PDF documents, extract text implicitly, generate concise summaries via NLP, and perform semantic sentiment analysis on the content.

---

## ✨ Key Features

- **Asynchronous Processing**: Heavy AI tasks (PDF parsing, text summarizing) are offloaded to Celery workers to guarantee lightning-fast API responses.
- **AI-Powered Insights**: Integrates `PyPDF2` for text extraction, `Sumy` (LexRank algorithm) for automated summarization, and `TextBlob` for emotional sentiment analysis.
- **RESTful Architecture**: Fully structured CRUD operations constructed via `ModelViewSets`.
- **Auto-Generated Documentation**: Real-time interactive API docs powered by Swagger UI (`drf-spectacular`).
- **Granular Security**: Strictly enforced object-level permissions ensure users can solely view and modify their own documents.

---

## 🛠 Tech Stack

- **Web Framework**: Django & Django Rest Framework (DRF)
- **Task Queue & Broker**: Celery & Redis
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **AI / NLP Components**: Sumy, TextBlob, NLTK
- **Documentation**: Swagger UI / OpenAPI 3.0

---

## ⚙️ Getting Started

Follow these instructions to get a local copy of the project up and running.

### Prerequisites

Ensure you have the following installed on your local machine:
- **Python 3.10+**
- **Redis Server** (`sudo apt install redis-server`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AlisherOP/Insight.git
   cd Insight
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**  
   Create a `.env` file in the root directory (where `manage.py` is located) and add the following:
   ```env
   DEBUG=True
   SECRET_KEY='your-secret-key-goes-here'
   CELERY_BROKER=redis://localhost:6379/0
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

---

## 🚀 Running the Application (Local Development)

To run the application locally, you need three distinct terminal windows running concurrently.

### 1. Start Redis Server
Ensure your Redis message broker is running in the background.
```bash
sudo systemctl start redis-server
# Verify it's running with: redis-cli ping (Should return PONG)
```

### 2. Start the Celery Worker
Open a **second terminal**, activate your virtual environment, and launch the Celery worker to intercept background tasks.
```bash
celery -A Insight worker --loglevel=info
```

### 3. Start the Django Server
Open a **third terminal**, activate your virtual environment, and launch the API.
```bash
python manage.py runserver
```

---

## 📚 API Documentation

Once the Django development server is running, you can access the interactive Swagger UI.

- **Swagger UI**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/) 

### Main Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/documents/` | Upload a new PDF document for AI processing |
| `GET` | `/api/documents/` | List all documents belonging to the authenticated user |
| `GET` | `/api/documents/{id}/` | Retrieve the result of a specific analyzed document |
| `DELETE` | `/api/documents/{id}/` | Delete a document |

---

## 🌍 Deployment (Production)

To deploy Insight AI professionally on a cloud provider (e.g., AWS, DigitalOcean, Linode), avoid using the built-in `runserver`. Instead, use a production-ready stack:

### Recommended Architecture
1. **Gunicorn**: Serves the Django application (WSGI).
2. **Nginx**: Acts as a reverse proxy, handling static/media files and routing requests to Gunicorn.
3. **Manager**: Systemd / Supervisor to manage Gunicorn and Celery processes.
4. **PostgreSQL**: Replaces the local SQLite database for handling massive concurrency safely.

### Deployment Checklist

1. **Setup PostgreSQL**: Update your `DATABASES` setting in `settings.py` to point to a PostgreSQL instance. Install `psycopg2-binary`.
2. **Configure Static Files**: Run `python manage.py collectstatic` to gather static assets for Nginx.
3. **Turn off DEBUG Mode**: In your `.env` file, critically set `DEBUG=False` and update `ALLOWED_HOSTS` with your domain/IP.
4. **Deploy Gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn --workers 3 Insight.wsgi:application
   ```
5. **Daemonizing Celery**: Create a Systemd service file (e.g., `/etc/systemd/system/celery.service`) to ensure your AI background tasks boot up automatically with the server and survive crashes.
6. **Daemonizing Redis**: Ensure Redis runs continuously (`sudo systemctl enable redis-server`).

> **💡 Best Practice**: Consider containerizing the application using **Docker** and **Docker Compose**. This will allow you to package Django, Celery, and Redis into separate, deployment-ready containers, eliminating environment disparities between development and production.

---

## 📝 License

Distributed under the MIT License.