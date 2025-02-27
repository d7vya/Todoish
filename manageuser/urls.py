from django.urls import path
from manageuser import views
urlpatterns = [
    path('', views.registeruser,name='register'),
    path('login', views.loginuser,name='login'),
    path('logout',views.userlogout,name='logout')
]
