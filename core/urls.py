from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name='login'), # Root now opens login
    path('home/', views.home, name='home'),   # Home moved to /home/
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
