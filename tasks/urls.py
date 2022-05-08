from django.urls import path
from tasks import views
app_name = "tasks"
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
]
