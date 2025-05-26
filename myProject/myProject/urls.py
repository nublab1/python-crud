
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('sign_up/', signupPage, name='signup'),
    path('login/',loginPage,name='login'),
    path('student/', student_view, name='student'),
    path('student/create/', student_create, name='student_create'),
    path('student/<int:id>/', student_detail, name='student_view'),
    path('student/<int:id>/edit/', student_edit, name='student_edit'),
    path('student/<int:id>/delete/', student_delete, name='student_delete'),
    path('teacher/', teacher_view, name='teacher'),
    path('teacher/create/', teacher_create, name='teacher_create'),
    path('teacher/<int:id>/', teacher_detail, name='teacher_view'),
    path('teacher_edit/<int:id>/',teacher_edit ,name='teacher_edit'),
    path('teacher/delete/<int:id>/', teacher_delete, name='teacher_delete'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)