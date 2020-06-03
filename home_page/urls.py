from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_course', views.add_course, name='add_course'),
    path('view_course_form', views.view_course_form, name='view_course_form'),
#    url(r'^delete/(\d+)/$',views.view_course_form,name="delete_course"),
    path('delete_course/<int:course_id>/',views.delete_course,name="delete_course")
]