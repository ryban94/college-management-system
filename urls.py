from django.urls import path
from Student import views

urlpatterns = [
    path('index/', views.indexpage, name="indexpage"),
    path('stud_profile/',views.stud_profile,name="stud_profile"),
    path('stud_edit/',views.stud_edit,name="stud_edit"),
    path('stud_save/',views.stud_save,name="stud_save"),
    path('stud_notification/',views.stud_notification,name="stud_notification"),
    path('stud_user/',views.stud_user,name="stud_user"),
    path('stud_login/',views.stud_login,name="stud_login")


]