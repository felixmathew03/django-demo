from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('students/',views.students,name='view_students'),
    path('students/<int:id>/',views.get_student),
    path('students/<int:id>/edit/',views.edit_student),
    path('students/<int:id>/delete/',views.delete_student),
    path('add/',views.add_student)
]