from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,"studentindex.html")
def stud_profile(request):
    return render(request,"student_profile.html")

def stud_edit(request):
    return render(request,"student_edit.html")