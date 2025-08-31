from pydantic import BaseModel , Field , EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = "John Doe"
    age: int
    grade: Optional[str] = None
    email: EmailStr
    cgpa:float = Field(gt=0.0, lt=10.0,default=5,description="this is student's cgpa score")

#Type Coercion: Pydantic will attempt to coerce the string into an integer.
new_student = {'age':30,"grade":"FY", 'email':"abs@gamil.com","cgpa":8.5}
student = Student(**new_student)
print(student)  
print(student.age)  

student_dict = dict(student)
print("Dict = ",student_dict)
print(student_dict["age"]) 

student_json = student.model_dump_json()
print("json = ",student_json)