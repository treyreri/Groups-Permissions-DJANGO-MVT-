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



#lesson
@permission_required('myapp.view_lesson' , raise_exception = True)
def lesson_list(request):
    lessons = Lesson.objects.all()

    return render(request, 'lesson_list.html' , {'lessons' : lessons})

@permission_required('myapp.view_lesson', raise_exception = True)
def lesson_detail(request ,id):
    lesson = get_object_or_404(Lesson, id = id )
    return render (request, 'lesson_detail.html', {'lesson' : lesson})

@permission_required('myapp.add_lesson', raise_exception = True)
def lesson_create(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        course_id = request.POST.get('course')

        course = get_object_or_404(Course, id = course_id)

        Lesson.objects.create(title = title , content = content, course = course)
        return redirect('lesson_list')
    return render(request, 'lesson_form.html' , {'courses' : courses})

@permission_required('myapp.change_lesson', raise_exception=True)
def lesson_update(request, id):
    lesson = get_object_or_404(Lesson, id = id)
    courses = Course.objects.all()

    if request.method == 'POST':
        lesson.title = request.POST.get('title')
        lesson.content = request.POST.get('content')
        course_id = request.POST.get('course')

        lesson.course = get_object_or_404(Course, id=course_id)

        lesson.save()

        return redirect('lesson_detail' , id = lesson.id)
    return render(request, 'lesson_form.html' , {'lesson' : lesson, 'courses' : courses})

@permission_required('myapp.delete_lesson', raise_exception = True)
def lesson_delete(request, id):
    lesson = get_object_or_404(Lesson, id = id)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list')
    return render(request, 'lesson_delete.html' , {'lesson' : lesson} )



#comment
@permission_required('myapp.view_comment', raise_exception=True)
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment_list.html', {'comments' : comments})

@permission_required('myapp.view_comment' , raise_exception = True)
def comment_detail(request, id):
    comment = get_object_or_404(Comment, id = id)
    return render(request, 'comment_detail.html' , {'comment' : comment})

@permission_required('meapp.add_comment' , raise_exception = True)
def comment_create(request, lesson_id):
    lesson = get_object_or_404(Lesson, id = lesson_id)

    if request.method == 'POST':
        text = request.POST.get('text')

        Comment.objects.create(text = text , user = request.user, lesson = lesson)
        return redirect('lesson_detail' , id = lesson.id)
    return render(request, 'comment_form.html', {'lesson' : lesson})

@permission_required('myapp.change_comment', raise_exception=True)
def comment_update(request, id):
    comment = get_object_or_404(Comment, id = id)
    #админ может редактировать дюбой коммент, остальные пользователи только свои коммы
    if not request.user.is_superuser:
        if comment.user != request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied

    if request.method == 'POST':
        comment.text = request.POST.get('text')
        comment.save()

        return redirect('comment_detail' , id = comment.id)

    return render(request, 'comment_form.html' , {'comment' : comment})

@permission_required('myapp.delete_comment', raise_exception = True)
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id = id)
    #админ может удалить любой коммент, остальные пользователи только свои коммы
    if not request.user.is_superuser:
        if comment.user != request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied

    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')

    return render(request, 'comment_delete.html' , {'comment' : comment})
