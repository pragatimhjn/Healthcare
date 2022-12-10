from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import staffdata,MyUserCreationForm
from .models import Doctors,Blog,Userinfo,Patients
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User,auth
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')
def userreg(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,"regi.html",{'f':form})
from django.contrib.sessions.models import Session
def login(request):
        if request.method == "POST":
                username1 = request.POST.get("username")
                password1 = request.POST.get("password")
                user = auth.authenticate(username=username1,password=password1)
                if user is not None and user.is_doctor:
                        auth.login(request,user)
                        request.session['is_logged'] = True
                        return redirect("doctor")

                elif user is not None and user.is_patient:
                        auth.login(request,user)
                        request.session['is_logged'] = True
                        return redirect("patient")
                        
                else: 
                        messages.info(request,"Username and Password Does Not Match!!!")
                        return redirect("login")
        else:
                return render(request,"login.html")
    
def doctor(request):
    return render(request,"doctor.html")

def patient(request):
    return render(request,"patient.html")

def logout(request):
        auth.logout(request)
        return redirect("index")

def allrecords(request):
    doctors = Doctors.objects.all()
    context = {
        'doctors': doctors,
    }
    print(context)
    return render(request, 'view_all_docs.html', context)
def allpatients(request):
    patients = Patients.objects.all()
    context = {
        'patients': patients,
    }
    print(context)
    return render(request, 'view_all_patients.html', context)
def add_patient(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenum = int(request.POST['phonenum'])
        treat_dept = request.POST['treat_dept']
        address = request.POST['address']
        emailid = request.POST['emailid']
        bloodgroup = request.POST['bloodgroup']

        patient = Patients(firstname=firstname, lastname=lastname, phonenum=phonenum, treat_dept= treat_dept,address=address,emailid=emailid,bloodgroup=bloodgroup)
        patient.save()
        #return HttpResponse('Patient added Successfully')
        return redirect('all_patient_records')
    elif request.method=='GET':
        return render(request, 'add_patient.html')
    else:
        return HttpResponse("An Exception Occured! Patient Has Not Been Added")


def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        phone = int(request.POST['phone'])
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']
        doctor = Doctors(first_name=first_name, last_name=last_name, salary=salary, phone=phone, dept= dept, role= role,location=location, hire_date = datetime.now())
        doctor.save()
        #return HttpResponse('Doctor added Successfully')
        return redirect('all_records')
    elif request.method=='GET':
        return render(request, 'add.html')
    else:
        return HttpResponse("An Exception Occured! Doctor Has Not Been Added")

def delete(request, doc_id = 0):
    if doc_id:
        try:
            doc_to_be_removed = Doctors.objects.get(id=doc_id)
            doc_to_be_removed.delete()
            #return HttpResponse("Employee Removed Successfully")
            return redirect('all_records')
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    doctors = Doctors.objects.all()
    context = {
        'doctors': doctors,
    }
    return render(request, 'remove.html',context)

def update(request, doc_id=0):
    if doc_id:
        try:
            doctor = Doctors.objects.get(id=doc_id)
            template = loader.get_template('update.html')  
            context = {
            'doctor': doctor,
                }
            return HttpResponse(template.render(context, request))
  
        except:
            return HttpResponse("Please Enter VALID ID")
    doctors = Doctors.objects.all()
    context = {
        'doctors': doctors,
    }
    return render(request, 'update1.html',context)
  
  
def updaterecord(request, doc_id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    salary = int(request.POST['salary'])
    phone = int(request.POST['phone'])
    dept = request.POST['dept']
    role = request.POST['role']
    location = request.POST['location']

    doctor=Doctors.objects.get(id=doc_id)
    doctor.first_name = first_name
    doctor.last_name = last_name
    doctor.salary = salary
    doctor.phone = phone
    doctor.dept = dept
    doctor.role = role
    doctor.location = location
    doctor.save()
    return redirect('all_records')

def filter_doc(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']
        doctors = Doctors.objects.all()
        if name:
            doctors = doctors.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))

        if dept:
            doctors = doctors.filter(dept__icontains = dept)
        if role:
            doctors = doctors.filter(role__icontains = role)
        if location:
           doctors = doctors.filter(location__icontains = location)

        context = {
            'doctors': doctors
            }
        print(context)
        return render(request, 'view_all_docs.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_doc.html')
    else:
        return HttpResponse('An Exception Occurred')
def staff_input_view(request):
        form2 = staffdata(request.POST or None)
        if request.method == "POST" and form2.is_valid():

                    name = form2.cleaned_data['name']
                    sid = form2.cleaned_data['sid']

                    print(name)
                    print(sid)
                    return render(request,"see1.html", {"name":name,"sid":sid})

        return render(request,"staffdata.html",{"form2":form2})


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request,"bloghome.html",context)


def blogpost(request,slug):
    blog = Blog.objects.get(slug=slug)
    context = {
            'blog': blog,
                }

    return render(request,"blogpost.html",context)

    # return HttpResponse(f'You are viewing {slug}')
    



