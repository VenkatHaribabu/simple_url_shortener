# Simple URL Shortener
# Overview

This project is an asynchronous URL Shortener built using **Python**, **Flask**, **Redis**, **Celery**, **SQLite**, and **Marshmallow**.

When a user submits a URL:

A unique short code is generated.
The URL is stored in the SQLite database with the status **pending**.
A background task is sent to Celery using Redis.
The Celery worker validates the URL and updates the status to **active** or **invalid**.
Users can retrieve the URL information using the generated short code.

---

# Technologies Used

* Python
* Flask
* Redis
* Celery
* SQLite
* Marshmallow

---

# Project Structure

```text
simple_url_shortener/
    app/
    │
    ├──instance/
    |    └── urls.db
    ├── app.py
    ├── celery_worker.py
    ├── config.py
    ├── database.py
    ├── init_db.py
    ├── models.py
    ├── README.md
    ├── requirements.txt
    ├── routes.py
    ├── schemas.py
    ├── tasks.py
    ├── utils.py
    ```

---

# Setup Instructions

1. Clone the Repository
git clone <repository-url>
cd simple_url_shortener


```bash
cd simple_url_shortener/app
```

# 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

# 4. Create the Database

```bash
python init_db.py
```

# 5. Start Redis

```bash
redis-server
```

# 6. Start the Celery Worker

```bash
celery -A celery_worker worker --pool=solo --loglevel=info
```

# 7. Start the Flask Application

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

---

# API Endpoints

# 1. Create Short URL

**POST** `/shorten`

Request Body

```json
{
    "url": "https://example.com"
}
```

Response

```json
{
    "id": 1,
    "short_code": "Ab12Xy",
    "status": "pending"
}
```

---

# 2. Get URL Details

**GET** `/url/<short_code>`

Example

```text
GET /url/Ab12Xy
```

Response

```json
{
    "short_code": "Ab12Xy",
    "original_url": "https://example.com",
    "status": "active"
}
```

---

# Workflow

1. User sends a URL using **POST /shorten**.
2. Flask validates the request.
3. A unique short code is generated.
4. The URL is stored in SQLite with **pending** status.
5. A background task is sent to Celery through Redis.
6. Celery validates the URL.
7. The database status is updated to **active** or **invalid**.
8. User retrieves the URL details using **GET /url/<short_code>**.

---

# Database Schema

| Column       | Description                |
| ------------ | -------------------------- |
| id           | Auto-increment primary key |
| short_code   | Unique short code          |
| original_url | Original URL               |
| status       | pending / active / invalid |

---

# Sample cURL Commands

# Create Short URL

```bash
curl -X POST http://127.0.0.1:5000/shorten \
-H "Content-Type: application/json" \
-d "{\"url\":\"https://example.com/some/page\"}"
```

### Get URL Details

```bash
curl http://127.0.0.1:5000/url/Ab12Xy
```

