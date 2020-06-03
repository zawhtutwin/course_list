from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Course


def index(request):
	courses = Course.objects.all()
	return render(request, 'courses.html',{'courses':courses})

def view_course_form(request):
	return render(request,'course_form.html')

def add_course(request):
	course_code = str(request.POST.get("course_code"))
	semester = int(request.POST.get("semester"))
	Course.objects.create(course_code=course_code,semester=semester)
	return redirect("/")

def delete_course(request,course_id):
	course =Course.objects.get(pk = course_id)
	course.delete()
	return redirect("/")
