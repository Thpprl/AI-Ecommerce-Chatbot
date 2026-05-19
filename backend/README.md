# CPE420-BE - Chat API Backend

FastAPI application providing chat endpoints with AI model integration.

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd CPE420-BE
```

2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

### Development Server
```bash
uvicorn app.main:app --reload
```

The server will start at `http://localhost:8000`

### API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
app/
├── main.py              # FastAPI application setup
├── api/
│   └── v1/
│       └── chat.py      # Chat endpoints
├── core/
│   └── ai_model.py      # AI model integration
├── schemas/
│   └── chat_schema.py   # Request/response schemas
└── services/
    └── chat_service.py  # Chat business logic
```

## API Endpoints

- **Chat API**: `/api/v1/chat` (see Swagger docs for details)

## Configuration

The API is configured to accept requests from:
- `http://localhost:4200`
- `http://127.0.0.1:4200`

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Other dependencies (see requirements.txt)
