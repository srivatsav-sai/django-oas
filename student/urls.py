from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib import admin

from .views import(
	student,
	quick_appointmnet,
	appointment_book,
	)

urlpatterns = [
    path('', views.student, name='customer'),
    path('my_appointment/', views.student, name='customer'),
    path('quick_appointmnet/', views.quick_appointmnet, name='quick_appointmnet'),   
    path('update/<int:id>/', views.appointment_book,name='appointment_update'),
    path('homepage/', TemplateView.as_view(template_name='static_pages/homepage.html'), name='homepage'),
    path('contact/', TemplateView.as_view(template_name='static_pages/contact.html'), name='contact'),
    path('about/', TemplateView.as_view(template_name='static_pages/about.html'), name='about'),
    path('lawyer_a/', TemplateView.as_view(template_name='static_pages/lawyer_a.html'), name='lawyer_a'),
    path('Lawyer2/', TemplateView.as_view(template_name='static_pages/Lawyer2.html'), name='Lawyer2'),
    path('Lawyer3/', TemplateView.as_view(template_name='static_pages/Lawyer3.html'), name='Lawyer3'),
    path('Lawyer4/', TemplateView.as_view(template_name='static_pages/Lawyer4.html'), name='Lawyer4'),
]
