from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    course_id = models.IntegerField()
    course_title = models.CharField(max_length=50)
    course_image = models.ImageField(
        upload_to='images/', default='lms/media/images/img03098-p1c4ja9s6v131m1ilh1bq8661273.jpg')
    # subcourse1_comp = models.IntegerField(default=0)
    # subcourse2_comp = models.IntegerField(default=0)
    # subcourse3_comp = models.IntegerField(default=0)
    # subcourse4_comp = models.IntegerField(default=0)
    
class SubCourse(models.Model):
    course_id = models.IntegerField()
    sub_course_no = models.IntegerField()
    video1 = models.FileField(upload_to='videos/')
    video2 = models.FileField(upload_to='videos/')
    video3 = models.FileField(upload_to='videos/')
    video4 = models.FileField(upload_to='videos/')
    transcript = models.FileField(upload_to='trans/')
    # quiz_marks = models.IntegerField()
    mandatory = models.BooleanField()

class Score(models.Model):
    course_id = models.IntegerField()
    sub_course_no = models.IntegerField()
    student = models.ForeignKey(User,on_delete=models.CASCADE)

class Student(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    course_id = models.IntegerField()
    completed = models.IntegerField()





