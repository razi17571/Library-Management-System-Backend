```markdown
# Library Management System Backend

This is the backend layer of the Library Management System, implemented using FastAPI and MongoDB.

## Tech Stack

- Language: Python
- Framework: FastAPI
- Database: MongoDB (MongoDB Atlas M0 Free Cluster)

## Deployment

This application is deployed on Render and is live at [https://library-management-system-backend-7br0.onrender.com](https://library-management-system-backend-7br0.onrender.com).

Make sure to replace `<Your MongoDB Atlas Connection String>` with the actual connection string of your MongoDB Atlas cluster.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/razi17571/Library-Management-System-Backend.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally:

```bash
uvicorn main:app --reload
```

The application will start running at `http://127.0.0.1:8000`.

## API Documentation

You can access the API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## Endpoints

- `POST /students`: Create a new student.
- `GET /students`: List all students with optional filters.
- `GET /students/{id}`: Get details of a specific student by ID.
- `PATCH /students/{id}`: Update details of a specific student by ID.
- `DELETE /students/{id}`: Delete a specific student by ID.

## CORS Configuration

By default, CORS is enabled to accept requests from all origins. You can adjust CORS configuration in `main.py` as needed.


```