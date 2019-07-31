"""myproject URL Configuration

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
from django.urls import path
import cau_quiz.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cau_quiz.views.home, name='home'),
    path('createPlayer', cau_quiz.views.createPlayer, name='createPlayer'),
    path('index/<int:quiz_id>', cau_quiz.views.index, name='index'),
    #path('move/', quiz.views.move, name='move'),
    path('answer/<int:quiz_id>', cau_quiz.views.answer, name='answer'),
    path('endgame/', cau_quiz.views.endgame, name='endgame'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)