"""
URL configuration for studentproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from students import views

urlpatterns = [
    path('',views.user_login,name="login"),
    path('students/',views.student_list, name='student_list'),
    path('add/',views.add_student,name="add_student"),
    path('update/<int:id>/',views.update_student,name="update_student"),
    path('delete/<int:id>/',views.delete_student,name="delete_student"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]