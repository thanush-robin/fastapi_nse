# FastAPI NSE Strategy Dashboard 

This is a FastAPI-based backend for managing a **mean reversion strategy** 
used in stock analysis. It provides APIs for creating, updating, retrieving, and deleting strategy configurations using SQLite as the database.

---

## Features

- **CRUD operations** for strategy management (`POST`, `GET`, `PUT`, `DELETE`)
- **Validation** for fields like dates and strategy type
- **Auto-incrementing IDs**
- **SQLite integration**
- Clean and modular code with SQLAlchemy + Pydantic

---

## Project Structure
fastapi_nse_project/
│
├── main.py # FastAPI app with endpoints
├── models.py # SQLAlchemy models
├── schema.py # Pydantic schemas
├── crud.py # Database operations
├── database.py # Database connection
└── README.md # Project documentation

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/thanush-robin/fastapi_nse.git
cd fastapi_nse
2. Create and Activate a Virtual Environment (Optional)
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt, install manually:

bash
Copy
Edit
pip install fastapi uvicorn sqlalchemy pydantic
4. Run the FastAPI Server
bash
Copy
Edit
uvicorn main:app --reload
Visit: http://localhost:8000/docs for the Swagger API UI.




