from django.urls import path

from . import views

urlpatterns = [
    #home
    path('', views.home, name = 'home') , 

    #course
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:id>/update/', views.course_update, name='course_update'),
    path('courses/<int:id>/delete/', views.course_delete, name='course_delete'),

    #lesson
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/<int:id>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/create/', views.lesson_create, name='lesson_create'),
    path('lessons/<int:id>/update/', views.lesson_update, name='lesson_update'),
    path('lessons/<int:id>/delete/', views.lesson_delete, name='lesson_delete'),

    #comment
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:id>/', views.comment_detail, name='comment_detail'),
    path ('lessons/<int:lesson_id>/comments/create/', views.comment_create, name='comment_create')

    path ('lessons/<int:lesson_id>/comments/create/', views.comment_create, name='comment_create')

    path('comments/<int:id>/update/', views.comment_update, name='comment_update')

    path('comments/<int:id>/delete/',views.comment_delete,name='comment_delete') , ]