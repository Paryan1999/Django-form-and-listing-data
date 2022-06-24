from django.urls import path
from .import views


urlpatterns = [
    path("",views.student_form),
    path("list/",views.student_list),
]
