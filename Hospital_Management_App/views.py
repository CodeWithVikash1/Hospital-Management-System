from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def patient_login(request):
    error = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        try:
            Patient.objects.get(user=user)
            login(request, user)
            error = "no"
        except:
                error = "yes"
        
    return render(request,'patient_login.html',{'error':error})

def patient_signup(request):
    error = ""
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('email')
        password = request.POST.get('password1')
        
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        if User.objects.filter(username=username).exists():
            error = "not"
        else:
            try:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password)
                Patient.objects.create(user=user,age=age,contact=contact,gender=gender,address=address)
                error = "no"
            except:
                error = "yes"
    return render(request,'patient_signup.html',{'error':error})

def admin_login(request):
    error = ""
    if request.method == "POST":
        username =  request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'admin_login.html',{'error':error})

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    total_doctors = Doctor.objects.all().count()
    approved_doctors = Doctor.objects.filter(status='Approved').count()
    total_patients = Patient.objects.all().count()
    total_appointments = Appointment.objects.all().count
    return render(request, 'admin_home.html',{'total_doctors':total_doctors,'approved_doctors':approved_doctors,'total_patients':total_patients,'total_appointments':total_appointments})

def logout_admin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not request.user.is_staff:
        return redirect('admin_login')
    logout(request)
    return redirect('index')

def logout_patient(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    logout(request)
    return redirect('index')

def logout_doctor(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    logout(request)
    return redirect('index')

def patient_home(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    try:
        Patient.objects.get(user=request.user)
    except:
        return redirect('patient_login')
    return render(request,'patient_home.html')

def doctor_login(request):
    error = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user is not None:
            try:
                doctor = Doctor.objects.get(user=user)
                if doctor.status == "Approved":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
    return render(request,'doctor_login.html',{'error':error})

def doctor_signup(request):
    error = ""
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('email')
        password = request.POST.get('password1')
        
        gender = request.POST.get('gender')
        specialization = request.POST.get('specialization')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        
        if User.objects.filter(username=username).exists():
            error = "not"
        else:
            try:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password)
                Doctor.objects.create(user=user,specialization=specialization,contact=contact,gender=gender,address=address,status="Pending")
                error = "no"
            except:
                error = "yes"
    return render(request,'doctor_signup.html',{'error':error})

def doctor_home(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    return render(request,'doctor_home.html')

def pending_doctors(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctors = Doctor.objects.filter(status='Pending')
    return render(request,'pending_doctors.html',{'doctors':doctors})

def approved_doctors(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctors = Doctor.objects.filter(status='Approved')
    return render(request,'approved_doctors.html',{'doctors':doctors})

def rejected_doctors(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctors = Doctor.objects.filter(status='Rejected')
    return render(request,'rejected_doctors.html',{'doctors':doctors})

def all_doctors(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctors = Doctor.objects.all()
    return render(request,'all_doctors.html',{'doctors':doctors})

def approve_doctor(request,pk):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor = Doctor.objects.get(id=pk)
    error = ""
    try:
        doctor.status = "Approved"
        doctor.save()
        error = "no"
    except:
        error = "yes"
    return render(request,'pending_doctors.html',{'error':error})
    

def reject_doctor(request,pk):
    if request.user.is_staff:
        return redirect('admin_login')
    doctor = Doctor.objects.get(id=pk)
    error = ""
    try:
        doctor.status = "Rejected"
        doctor.save()
        error = "no"
    except:
        error = "yes"
    return render(request,'pending_doctors.html',{'error':error})
    
def delete_doctor(request,pk):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor = Doctor.objects.get(id=pk)
    user = doctor.user
    user.delete()
    doctor.delete()
    return redirect('all_doctors')

def view_patients(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    patients = Patient.objects.all()
    return render(request,'view_patients.html',{'patients':patients})
    
def delete_patient(request,pk):
    if not request.user.is_staff:
        return redirect('admin_login')
    patient = Patient.objects.get(id=pk)
    user = patient.user
    user.delete()
    patient.delete()
    return redirect('view_patients')

def view_appointments(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    appointments = Appointment.objects.all()
    return render(request,'view_appointments.html',{'appointments':appointments})

def book_appointment(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    error = ""
    doctors = Doctor.objects.filter(status="Approved")
    if request.method == "POST":
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            patient = Patient.objects.get(user=request.user)
            Appointment.objects.create(doctor=doctor,patient=patient,date=date,time=time,description=description,status='Pending')
            error = "no"
        except:
            error = "yes"
            
    return render(request,'book_appointment.html',{'doctors':doctors,'error':error})

def my_appointments(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient).order_by('-date', '-time')
    return render(request,'my_appointments.html',{'appointments':appointments})

def patient_view_profile(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    patient = Patient.objects.get(user=request.user)
    return render(request,'patient_view_profile.html',{'patient':patient})

def patient_edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    patient = Patient.objects.get(user=request.user)
    error = ""
    if request.method == "POST":
        try:
            user = request.user
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.contact = request.POST.get('contact')
            patient.address = request.POST.get('address')
            patient.save()
            error = "no"
            
        except:
            error = "yes"
        
    return render(request,'patient_edit_profile.html',{'patient':patient,'error':error})

def pending_appointments(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor =  Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    
    appointments = Appointment.objects.filter(doctor=doctor, status='Pending').order_by('date', 'time')
    return render(request,'pending_appointments.html',{'appointments':appointments})

def approved_appointments(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor = Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointments = Appointment.objects.filter(doctor=doctor,status='Approved').order_by('date', 'time')
    return render(request,'approved_appointments.html',{'appointments':appointments})

def rejected_appointments(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor =  Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointments = Appointment.objects.filter(doctor=doctor,status='Declined').order_by('date', 'time')
    
    return render(request,'rejected_appointments.html',{'appointments':appointments})

def completed_appointments(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor =  Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointments = Appointment.objects.filter(doctor=doctor,status='Completed').order_by('date', 'time')
    
    return render(request,'completed_appointments.html',{'appointments':appointments})

def all_appointments(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor = Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date', 'time')
    return render(request,'all_appointments.html',{'appointments':appointments})

def approve_appointment(request,pk):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointment = Appointment.objects.get(id=pk)
    error = ""
    try:
        appointment.status = "Approved"
        appointment.save()
        error = "no"
    except:
        error = "yes"
    return render(request,'pending_appointments.html',{'error':error})

def decline_appointment(request,pk):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointment = Appointment.objects.get(id=pk)
    error = ""
    try:
        appointment.status = "Declined"
        appointment.save()
        error = "no"
    except:
        error = "yes"
    return render(request,'pending_appointments.html',{'error':error})

def complete_appointment(request,pk):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointment = Appointment.objects.get(id=pk)
    error = ""
    try:
        appointment.status = "Completed"
        appointment.save()
        error = "not"
    except:
        error = "cancel"
    return render(request,'view_doctor_appointments.html',{'error':error})

def view_doctor_appointments(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor = Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointments = Appointment.objects.filter(doctor=doctor,status='Approved').order_by('date', 'time')
    return render(request,'view_doctor_appointments.html',{'appointments':appointments})

def patients_list(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor = Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    appointments = Appointment.objects.filter(doctor=doctor).select_related('patient')
    patients = list(set([appt.patient for appt in appointments]))
    return render(request,'patients_list.html',{'patients':patients})

def doctor_view_profile(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor = Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    return render(request,'doctor_view_profile.html',{'doctor':doctor})

def doctor_edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    try:
        doctor = Doctor.objects.get(user=request.user)
    except:
        return redirect('doctor_login')
    error = ""
    if request.method == "POST":
        try:
            user = request.user
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            
            doctor.gender = request.POST.get('gender')
            doctor.contact = request.POST.get('contact')
            doctor.address = request.POST.get('address')
            doctor.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'doctor_edit_profile.html',{'error':error,'doctor':doctor})    
        