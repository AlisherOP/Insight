# 🧠 Insight AI - Document Analysis Engine

An asynchronous backend API built with **Django Rest Framework**, **Celery**, and **Redis** that extracts text from PDFs and provides AI-powered summaries and sentiment analysis.

## 🚀 Key Features
- **Asynchronous Processing**: Heavy AI tasks are offloaded to Celery workers to keep the API responsive.
- **AI Integration**: Uses `PyPDF2` for extraction, `Sumy` (LexRank) for summarization, and `TextBlob` for sentiment analysis.
- **RESTful Architecture**: Complete CRUD operations via `ModelViewSets`.
- **Auto-Documentation**: Interactive API docs via Swagger (drf-spectacular).
- **Security**: Object-level permissions (users only see their own documents).

## 🛠️ Tech Stack
- **Framework**: Django & DRF
- **Task Queue**: Celery & Redis
- **Database**: PostgreSQL (Production) / SQLite (Dev)
- **AI/NLP**: Sumy, TextBlob, NLTK
- **Docs**: Swagger UI

## 📦 Installation & Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/insight-ai.git
   cd insight-ai

    Setup Virtual Environment:
    code Bash

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt

    Start Redis:
    Ensure Redis is running on localhost:6379.

    Run the Engines (3 Terminals):

        Terminal 1 (Django): python manage.py runserver

        Terminal 2 (Celery): celery -A Insight worker --loglevel=info

        Terminal 3 (Redis): redis-server

📡 API Endpoints

    POST /api/documents/ - Upload PDF

    GET /api/documents/ - List user documents

    GET /api/docs/ - Interactive Swagger Documentation