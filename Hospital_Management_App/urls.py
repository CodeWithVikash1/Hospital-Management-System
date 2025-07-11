from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('patient_login/',views.patient_login,name='patient_login'),
    path('patient_signup/',views.patient_signup,name='patient_signup'),
    path('doctor_login/',views.doctor_login,name='doctor_login'),
    path('doctor_signup/',views.doctor_signup,name='doctor_signup'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('logout_admin/',views.logout_admin,name='logout_admin'),
    path('logout_patient/',views.logout_patient,name='logout_patient'),
    path('logout_doctor/',views.logout_doctor,name='logout_doctor'),
    path('patient_home/',views.patient_home,name='patient_home'),
    path('doctor_home/',views.doctor_home,name='doctor_home'),
    path('pending_doctors/',views.pending_doctors,name='pending_doctors'),
    path('approved_doctors/',views.approved_doctors,name='approved_doctors'),
    path('rejected_doctors/',views.rejected_doctors,name='rejected_doctors'),
    path('all_doctors/',views.all_doctors,name='all_doctors'),
    path('approve_doctor/<int:pk>/',views.approve_doctor,name='approve_doctor'),
    path('reject_doctor/<int:pk>/',views.reject_doctor,name='reject_doctor'),
    path('delete_doctor/<int:pk>/',views.delete_doctor,name='delete_doctor'),
    path('view_patients/',views.view_patients,name='view_patients'),
    path('delete_patient/<int:pk>/',views.delete_patient,name='delete_patient'),
    path('view_appointments/',views.view_appointments,name='view_appointments'),
    path('book_appointment/',views.book_appointment,name='book_appointment'),
    path('my_appointments/',views.my_appointments,name='my_appointments'),
    path('patient_view_profile/',views.patient_view_profile,name='patient_view_profile'),
    path('patient_edit_profile/',views.patient_edit_profile,name='patient_edit_profile'),
    path('pending_appointments/',views.pending_appointments,name='pending_appointments'),
    path('approved_appointments/',views.approved_appointments,name='approved_appointments'),
    path('rejected_appointments/',views.rejected_appointments,name='rejected_appointments'),
    path('completed_appointments/',views.completed_appointments,name='completed_appointments'),
    path('all_appointments/',views.all_appointments,name='all_appointments'),
    path('approve_appointment/<int:pk>/',views.approve_appointment,name='approve_appointment'),
    path('decline_appointment/<int:pk>/',views.decline_appointment,name='decline_appointment'),
    path('complete_appointment/<int:pk>/',views.complete_appointment,name='complete_appointment'),
    path('view_doctor_appointments/',views.view_doctor_appointments,name='view_doctor_appointments'),
    path('patients_list/',views.patients_list,name='patients_list'),
    path('doctor_view_profile/',views.doctor_view_profile,name='doctor_view_profile'),
    path('doctor_edit_profile/',views.doctor_edit_profile,name='doctor_edit_profile'),
    
    
    

]