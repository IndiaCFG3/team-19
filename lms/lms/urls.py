"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import courses.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:course_id>/', courses.views.detail, name='detail'),
    path('accounts/', include('accounts.urls')),
    path('',courses.views.home,name='home'),
    path('mycourses/',courses.views.getmycourses,name='mycourses'),
    path('create/',courses.views.createcourse,name='createcourse'),
    path('register/<int:course_id>/',
         courses.views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
