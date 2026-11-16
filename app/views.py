from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student

def home(request): # http://localhost:8000/
    return render(request, 'app/index.html',{'std_name':'Akhil'})

def about(request): # http://localhost:8000/about/
    return render(request,'app/about.html')

def students(request): # http://localhost:8000/students/
    all_students = Student.objects.all()
    return render(request,'app/students.html',{'students':all_students})

def get_student(request,id):
    student = Student.objects.get(id=id)
    return render(request,'app/student.html',{'student':student})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = int(request.POST['age'])
        mark = int(request.POST['mark'])
        course = request.POST['course']
        Student.objects.create(name= name,age=age,mark=mark,course=course)
        
        return redirect('view_students')
    return render(request,'app/add_student.html')

def edit_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = int(request.POST['age'])
        student.mark = int(request.POST['mark'])
        student.course = request.POST['course']
        student.save()
        return redirect('view_students')
    return render(request,'app/edit.html',{'student':student})

def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_students')