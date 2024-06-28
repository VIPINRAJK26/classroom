"""
URL configuration for classroompro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from clsroom_app import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [  
    path('admin/', admin.site.urls),
    path('',views.Index.as_view(),name='index_view'),
    path('T/reg',views.TeacherRegisterView.as_view(),name='teacher_register_view'),
    path('Sreg',views.StudentRegisterView.as_view(),name='student_register_view'),
    path('login',views.LoginView.as_view(),name='login_view'),
    path('t/login',views.TeacherLoginView.as_view(),name='teacher_login'),
    path('s/login',views.StudentLoginView.as_view(),name='student_login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('teacher/class/<int:id>',views.TeahcerUploads.as_view(),name='teacher_uploads'),
    path('stu/class',views.StudentClass.as_view(),name='studcls_view'),
    path('more/<int:id>',views.TeacherMoreDetails.as_view(),name='more_view'),
    path('home',views.Home.as_view(),name='home_view'),
    # path('class',views.ClassView.as_view(),name='class_view'),
    path('details/<int:id>',views.DetailedView.as_view(),name='detailed_view'),
    path('delete/<int:id>',views.ClassDeleteView.as_view(),name='delete_view'),
    path('stud/view',views.StudView.as_view(),name='stud_view'),
    path('edit/<int:id>',views.EditDetails.as_view(),name='edit_view'),
    path('user/data',views.UserData.as_view(),name='user_data'),
    path('premium',views.TryPremium.as_view(),name='premium'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
