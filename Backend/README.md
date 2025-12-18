# SyncFloww API

**Professional AI-Powered Video Pre-Production Engine**

SyncFloww API is the high-performance backend powering the SyncFloww platform, an AI-driven suite designed to revolutionize short-form video pre-production. Built with scalability and enterprise-grade architecture in mind, this API orchestrates complex AI agent workflows, manages multi-brand assets, and handles real-time social media integration.

## 🚀 Key Capabilities

*   **Advanced AI Orchestration**: Utilizes `Celery` and `Redis` for asynchronous execution of AI agents (Scriptwriting, Captioning, Improvement), ensuring zero-blocking on the main thread.
*   **Multi-Brand Architecture**: Robust data modeling to support multiple brands per user, with isolated social media tokens and analytic streams.
*   **Secure Authentication**: Implements JWT verification middleware connecting seamlessly with **Supabase Auth**, maintaining a stateless and secure session layer.
*   **Scalable Database Schema**: Normalized PostgreSQL schema designed for high-volume data, including specialized tables for AI configurations, automation rules, and analytics time-series data.
*   **Production Ready**: Configured for railway/cloud deployment with `Gunicorn`, environment-based settings, and comprehensive security headers.

## 🛠️ Technical Stack

*   **Framework**: Django 5.0 + Django REST Framework
*   **Task Queue**: Celery + Redis
*   **Database**: PostgreSQL
*   **Authentication**: Supabase JWT Integration
*   **Deployment**: Docker / Railway compatible (Gunicorn + WhiteNoise)

## 📂 Project Structure

```
syncfloww/
├── syncfloww/          # Core settings and configuration
│   ├── settings/       # Split settings (base, dev, prod)
│   ├── celery.py       # Async task configuration
│   └── middleware.py   # JWT Auth middleware
├── users/              # Extended user profiles
├── projects/           # Video project management
├── ai_agents/          # AI model and agent definitions
├── social/             # Social account and brand management
├── automations/        # Automation rules engine
└── analytics/          # Daily analytics data
```

## ⚡ Getting Started

### Prerequisites

*   Python 3.10+
*   Redis (for Celery)
*   PostgreSQL

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd SyncFloww-api
    ```

2.  **Create virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment:**
    Create a `.env` file with your credentials:
    ```env
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:pass@localhost:5432/syncfloww
    REDIS_URL=redis://localhost:6379/0
    SUPABASE_URL=https://your-project.supabase.co
    ```

5.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Start Server:**
    ```bash
    # Development
    python manage.py runserver

    # Celery Worker
    celery -A syncfloww worker -l info
    ```

## 🤝 Contributing

Please ensure all new models are added to the relevant app and tests are included for new endpoints. Follow the existing modular structure.
