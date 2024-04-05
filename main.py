from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

# MongoDB Connection
client = MongoClient("mongodb+srv://admin:admin123@quiz.tfajnzy.mongodb.net/?retryWrites=true&w=majority&appName=Quiz")
db = client["library_management"]
students_collection = db["students"]

# FastAPI App
app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

# Models
class AddressModel(BaseModel):
    city: str
    country: str

class StudentCreateModel(BaseModel):
    name: str
    age: int
    address: AddressModel

class StudentUpdateModel(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[AddressModel] = None

class StudentResponseModel(BaseModel):
    id: str
    name: str
    age: int
    address: AddressModel

# API Endpoints
@app.post("/students", status_code=201, response_model=StudentResponseModel)
def create_student(student: StudentCreateModel):
    inserted_student = students_collection.insert_one(student.dict())
    return {"id": str(inserted_student.inserted_id), **student.dict()}

@app.get("/students", response_model=List[StudentResponseModel])
def list_students(country: Optional[str] = None, age: Optional[int] = None):
    filters = {}
    if country:
        filters["address.country"] = country
    if age:
        filters["age"] = {"$gte": age}

    students = students_collection.find(filters)
    return [{"id": str(student["_id"]), **student} for student in students]

@app.get("/students/{student_id}", response_model=StudentResponseModel)
def get_student(student_id: str):
    student = students_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return {"id": str(student["_id"]), **student}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.patch("/students/{student_id}", status_code=204)
def update_student(student_id: str, student: StudentUpdateModel):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    if update_data:
        students_collection.update_one({"_id": ObjectId(student_id)}, {"$set": update_data})
    return

@app.delete("/students/{student_id}", status_code=200)
def delete_student(student_id: str):
    result = students_collection.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count == 1:
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
