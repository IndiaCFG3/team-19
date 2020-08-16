from django.contrib import admin
from .models import Course,SubCourse,Student
# Register your models here.


admin.site.register(Course)
admin.site.register(SubCourse)
admin.site.register(Student)
