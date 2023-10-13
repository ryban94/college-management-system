from django.urls import path
from Student import views

urlpatterns = [
    path('index/', views.indexpage, name="indexpage"),
    path('stud_profile/',views.stud_profile,name="stud_profile"),
    path('stud_edit/',views.stud_edit,name="stud_edit"),

]