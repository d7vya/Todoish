from django.urls import path
from home import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('create',views.createtask,name='create task'),
    path('team',views.manageteam,name='manageteam'),
    path('teaminfo',views.teaminfo),
    path('teams/<str:teamcode>',views.jointeam),
    path('tasklist',views.tasklist,name='user task')

]
