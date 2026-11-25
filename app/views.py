from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student, Course
from django.db.models import Avg
from django.contrib.auth.decorators import login_required


def home(request):  # http://localhost:8000/
    students = Student.objects.all()
    total = students.count()
    passed = students.filter(mark__gte=35).count() 
    average = students.aggregate(avg=Avg('mark'))['avg'] or 0
    print(request.user.is_authenticated)
    context = {
        'total_students': total,
        'total_courses': Course.objects.count(),
        'average_mark': round(average),
        'pass_rate': round(passed / total * 100) if total else 0,
        'top_students': students.order_by('-mark')[:3],
        'recent_students': students.order_by('-id')[:5],
        'is_logged_in':request.user.is_authenticated
    }
    return render(request, 'app/index.html', context)


def about(request): # http://localhost:8000/about/
    return render(request,'app/about.html')

def students(request): # http://localhost:8000/students/
    if request.user.is_authenticated:
        course = request.GET.get('course')
        search = request.GET.get('search')
        all_students = Student.objects.all()
        if course:
            all_students=all_students.filter(course=course)
        if search:
            all_students = all_students.filter(name__icontains = search)
        courses = Course.objects.all()
        return render(request,'app/students.html',{'students':all_students,'courses':courses,'is_logged_in':request.user.is_authenticated})
    else:
        return redirect('home')
@login_required
def get_student(request,id):
    student = Student.objects.get(id=id)
    return render(request,'app/student.html',{'student':student})
@login_required
def add_student(request):
    if request.method == 'POST':
        image = request.FILES.get('profile')
        name = request.POST['name']
        age = int(request.POST['age'])
        mark = int(request.POST['mark'])
        course_id = request.POST['course']
        course = get_object_or_404(Course,id=course_id)
        print(course)
        Student.objects.create(name= name,age=age,mark=mark,course=course,image=image)
        return redirect('view_students')
    courses = Course.objects.all()
    return render(request,'app/add_student.html',{'courses':courses})
@login_required
def edit_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = int(request.POST['age'])
        student.mark = int(request.POST['mark'])
        student.course = get_object_or_404(Course,id=request.POST['course'])
        student.save()
        return redirect('view_students')
    courses = Course.objects.all()
    return render(request,'app/edit.html',
                  {'student':student,'courses':courses})
@login_required
def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_students')