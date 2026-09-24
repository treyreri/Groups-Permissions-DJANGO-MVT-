from django.shortcuts import render

# Create your views here.

from .permissions import permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .models import Course, Lesson, Comment

def home (request):
    return render(request, 'home.html')


#course
@permission_required('myapp.view_course' , raise_exception = True)
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html' , {'courses' : courses})


@permission_required('myapp.view_course' , raise_exception = True)
def course_detail(request, id):
    course = get_object_or_404(Course, id = id)

    return render(request, 'course_detail.html' , {'course' : course})

@permission_required('myapp.add_course' , raise_exception = True)
def course_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')


        Course.objects.create(title = title, description = description, price = price)
        return redirect('course_list')
    
    return render(request, 'course_form.html')



@permission_required('myapp.change_course', raise_exception = True)
def course_update(request, id):
    course = get_object_or_404(Course, id = id)

    if request.method == 'POST':
        course.title = request.POST.get('title')
        course.description = request.POST.get('description')
        course.price = request.POST.get('price')

        course.save()

        return redirect('course_detail' , id = course.id)
    return render(request, 'course_form.html', {'course' : course}) 


@permission_required('myapp.delete_course' , raise_exception = True)
def course_delete(request, id):
    course = get_object_or_404(Course, id= id)

    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_delete.html' , {'course' : course})