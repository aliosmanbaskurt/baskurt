from multiprocessing import context
from django.shortcuts import render

import Courses
from .models import Course,Category,Tag
from Teachers.models import Teacher
from django.contrib.auth.decorators import login_required
# Create your views here.


def course_list(request):
    courses = Course.objects.all()
    lastcourses=Course.objects.all().order_by('-date')[:4]
    cats= Category.objects.all()
    tags =Tag.objects.all()
    context ={
        'courses' : courses,
        'cats':cats,
        'tags':tags,
        'lastcourses':lastcourses
    }
    return render(request,'course_list.html', context)


def course_detail (request, category_slug,course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    courses = Course.objects.all().order_by('-date')[:4]
    cats= Category.objects.all()
    tags =Tag.objects.all()
    totalcourse=Course.objects.filter(category__slug=category_slug).count()
    lastcourses=Course.objects.all().order_by('-date')[:4]
    context ={
        'course': course,
        'cats':cats,
        'tags':tags,
        'courses':courses,
        'totalcourse':totalcourse,
        'lastcourses':lastcourses
    }
    
    return render(request , 'courses.html',context)


def category_detail (request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    cats= Category.objects.all()
    tags =Tag.objects.all()
    totalcourse=Course.objects.filter(category__slug=category_slug).count()
    lastcourses=Course.objects.all().order_by('-date')[:4]
    context ={
        'courses': courses,
        'cats':cats,
        'tags':tags,
        'totalcourse':totalcourse,
        'lastcourses':lastcourses

    }
    
    return render(request , 'course_list.html',context)


def tag_list(request,tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug)
    cats= Category.objects.all()
    tags =Tag.objects.all()
    lastcourses=Course.objects.all().order_by('-date')[:4]
    totaltag=Course.objects.all().filter(tags__slug=tag_slug).count()
    context ={
        'courses': courses,
        'cats':cats,
        'tags':tags,
        'lastcourses':lastcourses,
        'totaltag':totaltag,
      
    }
    
    return render(request , 'course_list.html',context)


def searchlist (request):
    courses = Course.objects.filter(name__contains = request.GET['search'])
    cats = Category.objects.all()
    tags = Tag.objects.all()
    
    context ={
        'courses': courses,
        'cats':cats,
        'tags':tags,
      
    }
    
    return render(request , 'course_list.html',context)