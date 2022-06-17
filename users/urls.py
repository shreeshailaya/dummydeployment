from django.urls import path
from users import views

urlpatterns = [
    path('login', views.loginfun, name='login'),
    path('logout', views.logoutfun, name='logout'),
    path('registration', views.registration, name='registration')
]

