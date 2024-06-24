"""
URL configuration for Scrappit project.

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
from Scrappit import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),  
    path('about/', views.about),
     path('contact/', views.contact),
    path('educational_resourses/', views.educational_resourses),
    path('scrap_price/', views.scrap_price),
    path('scrrrap_points/', views.scrrrap_points),
    path('feedback/', views.feedback),
    path('book/', views.book),
    path('save_en/', views.save_en, name='save_en'),
    path('save_review/', views.save_review, name='save_review'),
    path('save_pick/', views.save_pickup, name='save_pickup'),
    path('course/', views.course),
    path('course/<int:abc>', views.coursedetails),

]
