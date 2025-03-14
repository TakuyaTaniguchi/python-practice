# Python Practice - ToDo API

A simple ToDo API built with FastAPI to learn Python web development.

👉 **TypeScript/Ruby on Rails経験者向け学習ガイド**: [LEARNING_GUIDE.md](LEARNING_GUIDE.md)

## Features
- RESTful API with CRUD operations for ToDo items
- Data validation with Pydantic
- Simple in-memory database (for learning purposes)
- Async request handling

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn

## Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux
source venv/bin/activate
# On Windows
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```

## Testing
Once the server is running, you can:

1. Access the interactive API documentation at http://localhost:8000/docs
2. Run the test script to verify all endpoints:
   ```bash
   python test_api.py
   ```

## API Endpoints
- `GET /todos` - List all ToDo items
- `GET /todos/{id}` - Get a single ToDo item
- `POST /todos` - Create a new ToDo item
- `PUT /todos/{id}` - Update a ToDo item
- `DELETE /todos/{id}` - Delete a ToDo item
