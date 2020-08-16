from django.shortcuts import render, redirect, get_object_or_404
from .models import Course,SubCourse,Student
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    print(request.user)
    all_courses = Course.objects.raw('SELECT * FROM courses_course;')
    return render(request,'courses/home.html',{'t':all_courses})

@login_required
def getmycourses(request,errorfromcreate=None):
    print(errorfromcreate)
    student_course = Student.objects.filter(student=request.user).values()
    courseids = []
    for student in student_course:
        courseids.append(student['course_id'])
    student_course_details = Course.objects.filter(
        course_id__in=courseids).values()
    return render(request,'courses/mycourses.html',{'V':student_course_details,'num':[0,0,0]})

@login_required
def register(request,course_id):
    s = Student()
    s.student = request.user
    s.course_id = course_id
    s.completed = 0
    s.save()
    return redirect('home')

def detail(request,course_id):
    getcourse = get_object_or_404(Course, course_id=course_id)
    return render(request,'courses/detail.html',{'course':getcourse})

@login_required
def createcourse(request):
    if request.user.is_superuser:
        if request.method=='POST':
            c = request.POST['id']
            course = Course()
            course.course_id = c
            course.course_title = request.POST['title']
            course.save()
            subcourse1 = SubCourse()
            subcourse1.course_id = c
            subcourse1.sub_course_no = request.POST['sub_course_no1']
            subcourse1.video1 = request.FILES['video1.1']
            subcourse1.video2 = request.FILES['video1.2']
            subcourse1.video3 = request.FILES['video1.3']
            subcourse1.video4 = request.FILES['video1.4']
            subcourse1.transcript = request.FILES['transcript1']
            subcourse1.quiz = request.POST['quiz1']

            subcourse2 = SubCourse()
            subcourse2.course_id = c
            subcourse2.sub_course_no = request.POST['sub_course_no2']
            subcourse2.video1 = request.FILES['video2.1']
            subcourse2.video2 = request.FILES['video2.2']
            subcourse2.video3 = request.FILES['video2.3']
            subcourse2.video4 = request.FILES['video2.4']
            subcourse2.transcript = request.FILES['transcript2']
            subcourse2.quiz = request.POST['quiz2']
            
            subcourse3 = SubCourse()
            subcourse3.course_id = c
            subcourse3.sub_course_no = request.POST['sub_course_no3']
            subcourse3.video1 = request.FILES['video3.1']
            subcourse3.video2 = request.FILES['video3.2']
            subcourse3.video3 = request.FILES['video3.3']
            subcourse3.video4 = request.FILES['video3.4']
            subcourse3.transcript = request.FILES['transcript3']
            subcourse3.quiz = request.POST['quiz3']
            
            subcourse4 = SubCourse()
            subcourse4.course_id = c
            subcourse4.sub_course_no = request.POST['sub_course_no4']
            subcourse4.video1 = request.FILES['video4.1']
            subcourse4.video2 = request.FILES['video4.2']
            subcourse4.video3 = request.FILES['video4.3']
            subcourse4.video4 = request.FILES['video4.4']
            subcourse4.transcript = request.FILES['transcript4']
            subcourse4.quiz = request.POST['quiz4']
            
            subcourse4.save()
            subcourse2.save()
            subcourse3.save()


            return redirect('home')
        else:
            return render(request,'courses/createcourse.html')
    else:
        return getmycourses(request,'You are not an admin')

@login_required   
def displayallaboutcourse(request,course_id):
    getcourse = get_object_or_404(Course, course_id=course_id)
    getsubcourse1 = get_object_or_404(SubCourse, course_id=course_id,sub_course_no=1)
    getsubcourse2 = get_object_or_404(SubCourse, course_id=course_id,sub_course_no=2)
    getsubcourse3 = get_object_or_404(
        SubCourse, course_id=course_id, sub_course_no=3)
    getsubcourse4 = get_object_or_404(
        SubCourse, course_id=course_id, sub_course_no=4)

    return redirect('home')

