"""face_br URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from face_br import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('ajax/',views.ajax, name= 'ajax'),
    path('profile/', views.profile, name='profile'),
    path('scan/', views.scan, name='scan'),
    path('student/', views.savestudent, name='student'),
    path('delete_profile/<int:id>/', views.delete_profile, name='delete_profile'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),
    path('student_total/', views.student_total, name='student_total'),
    
    path('reset/', views.reset, name='reset'),
    # path('present/', views.present, name='present'),
    path('clear_history/', views.clear_history, name='clear_history'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)