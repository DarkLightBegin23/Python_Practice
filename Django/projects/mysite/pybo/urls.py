from django.urls import path
from . import views
from django.contrib import admin

app_name = 'pybo'

urlpatterns = [
     path('', views.index, name='index'),
     path('admin/', admin.site.urls),
     path('<int:question_id>/', views.detail, name='detail'),
     path('answer/create/<int:question_id>/', views.answer_create, name="answer_create"),
]
