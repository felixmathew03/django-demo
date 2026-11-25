from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about),
    path('students/',views.students,name='view_students'),
    path('students/<int:id>/',views.get_student),
    path('students/<int:id>/edit/',views.edit_student),
    path('students/<int:id>/delete/',views.delete_student),
    path('add/',views.add_student)  # http://127.0.0.1:8000/add
]
# http://127.0.0.1:8000/teachers/add