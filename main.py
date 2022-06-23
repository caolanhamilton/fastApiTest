from tkinter import N
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Gazza",
        "age": 33,
        "topic": "Python"
    },
    2: {
        "name": "Caolan",
        "age": 25,
        "topic": "Python"
    },
    3: {
        "name": "Caolan",
        "age": 26,
        "topic": "Future Caolan"
    }
}

class Student(BaseModel):
    name: str
    age: int
    topic: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    topic: Optional[str] = None

@app.get("/")
def index():
    return {"message": "Hello World"}

# @app.get("/get-student/{student_id}")
# def index(student_id: int = Path(None, description="Provide ID of student you want", gt=0)):
#     return students[student_id]

@app.get("/get-students")
def get_all_students():
    return students


@app.get("/get-student")
def get_student_by_name(name: Optional[str] = None):
    name_matches = {}
    for student_id in students:
        if students[student_id]["name"] == name:
              name_matches[student_id] = students[student_id]
    if len(name_matches)==0:
        return {"Data": "Not found"}
    return name_matches

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student: Student):
    if student_id in students:
        return {"Error": "Student with ID exists"}
    students[student_id] = student
    return student

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "No student with this ID, cannot update"}
    
    print(students[student_id].name)
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.topic != None:
        students[student_id].topic = student.topic

    return students[student_id]
    


