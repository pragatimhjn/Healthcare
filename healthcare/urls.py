from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_records',views.allrecords,name='all_records'),
    path('add/', views.add, name='add'),
    path('all_patient_records',views.allpatients,name='all_patient_records'),
    path('addpatient/',views.add_patient,name='addpatient'),
    path('delete/', views.delete, name='delete'),
    path('delete/<int:doc_id>', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('update/<int:doc_id>', views.update, name='update'),
    path('update/updaterecord/<int:doc_id>', views.updaterecord, name='updaterecord'),
    path('filter_doc', views.filter_doc, name='filter_doc'),
    path('stform/',views.staff_input_view,name='stdata'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.userreg, name='reg'),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('bloghome/', views.blog, name='bloghome'),

]