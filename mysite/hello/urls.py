from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('donate/', views.donate_view, name='donate'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('service/', views.service, name='service'),
    path('donation_success/', views.donation_success, name='donation_success'),

    path('dashboard/', views.donation_dashboard, name='donation_dashboard'),
]
