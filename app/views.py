from django.shortcuts import render
from django.http import HttpResponse
name = 'Akhil'
all_students = [
    {'name':'Akhil','age':20,'mark':80,'course':'BCA'},
    {'name':'Arun','age':20,'mark':40,'course':'BBA'},
    {'name':'Karthik','age':21,'mark':21,'course':'MBA'},
    {'name':'Jinu','age':22,'mark':45,'course':'BCOM'},
]
def home(request): # http://localhost:8000/
    return render(request, 'app/index.html',{'std_name':'Akhil'})

def about(request): # http://localhost:8000/about/
    return render(request,'app/about.html')

def students(request): # http://localhost:8000/students/
    return render(request,'app/students.html',{'students':all_students})

def get_student(request,name):
    std = None
    for student in all_students:
        if student['name'] == name:
            std = student
    return render(request,'app/student.html',{'name':name,'student':std})