from django.shortcuts import render,redirect
from AdminUI.models import StudentDB,DepartmentDB,CourseDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime


# Create your views here.
def indexpage(request):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(StudentId=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request,"studentindex.html",{'name':name,'course':course,'dept':dept})
def stud_profile(request):
    stud_id = request.session["username"]
    name = StudentDB.objects.get(StudentId=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request,"student_profile.html",{'name':name,'course':course,'dept':dept})

def stud_edit(request):
    stud_id =request.session["username"]
    name = StudentDB.objects.get(StudentId=stud_id)
    course = CourseDB.objects.get(CourseId=name.CourseId.CourseId)
    dept = DepartmentDB.objects.get(DeptId=course.DeptId.DeptId)
    return render(request,"student_edit.html",{'name':name,'course':course,'dept':dept})

def stud_save(request):
    if request.method=="POST":
        stud_id = request.POST.get('StudentId')
        stud_fname = request.POST.get('FirstName')
        stud_lname = request.POST.get('LastName')
        stud_dob = request.POST.get('DateOfBirth')
        date_objj = datetime.strptime(stud_dob, "%B %d, %Y")
        formatted_dob = date_objj.strftime("%Y-%m-%d")

        stud_gender = request.POST.get('Gender')
        stud_email = request.POST.get('Email')
        stud_mob = request.POST.get('ContactNo')
        stud_address = request.POST.get('Address')
        stud_gcontact = request.POST.get('GuardianContact')
        stud_gname = request.POST.get('GuardianName')
        stud_dept = request.POST.get('DeptName')
        stud_course = request.POST.get('CourseName')
        try:
            stud_image = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(stud_image.name,stud_image)
        except MultiValueDictKeyError:
            file = StudentDB.objects.get(StudentId=stud_id).Image
            print(file)
        if StudentDB.objects.filter(StudentId=stud_id).exists():
            StudentDB.objects.filter(StudentId=stud_id).update(FirstName=stud_fname,LastName=stud_lname,
                                                               DateOfBirth=formatted_dob,Gender=stud_gender,
                                                               Email=stud_email,ContactNo=stud_mob,Address=stud_address,
                                                               GuardianContact=stud_gcontact,GuardianName=stud_gname,
                                                               Image=file)
        else:
            stud_image = request.FILES['Image']
            obj=StudentDB(FirstName=stud_fname,LastName=stud_lname,
                          DateOfBirth=stud_dob,Gender=stud_gender,
                          Email=stud_email,ContactNo=stud_mob,Address=stud_address,
                          GuardianContact=stud_gcontact,GuardianName=stud_gname,
                          Image=stud_image)
            obj.save()
        return redirect(stud_profile)

def stud_notification(request):
    return render(request,'notification.html')

def stud_user(request):
    return render(request,'student_login.html')

def stud_login(request):
    if request.method=="POST":
        stud_id = request.POST.get('user_id')
        stud_pwd = request.POST.get('user_pwd')
        if StudentDB.objects.filter(StudentId=stud_id,ContactNo=stud_pwd).exists():
            request.session['username']=stud_id
            request.session['password']=stud_pwd
            messages.success(request,"Login successfully")
            return redirect(stud_profile)
        else:
            messages.error(request, "Invalid ID or Password")
            return  redirect(stud_user)
    else:
        messages.error(request,"Invalid ID or Password")
        return redirect(stud_user)

def stud_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(stud_user)






