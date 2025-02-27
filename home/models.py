from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Teams(models.Model):
    name=models.CharField("Team name", max_length=50)
    admins=models.ManyToManyField(User,related_name='useradmin')
    members=models.ManyToManyField(User, related_name='userteam')
    owner=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created=models.DateField( auto_now=False, auto_now_add=True)
    code=models.CharField(max_length=10,default='admin')
    class Meta:
        permissions=[('remove_member','can remove members'),('remove_admin','can remove admin power'),('add_admin','can give admin power')]


class Tasks(models.Model):
    title=models.CharField('Task title', max_length=50)
    desc=models.CharField('Task description', max_length=200)
    assigned_by=models.ForeignKey(User, on_delete=models.CASCADE,related_name='assigned_task')
    assigned_to=models.ManyToManyField(User,related_name='usertask')
    start_date=models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)
    end_date=models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)
    mark_important=models.BooleanField(default=False)
    status_choices=[('p','pending'),('c','complete'),('wip','work in progress')]
    status=models.CharField(choices=status_choices,default='pending', max_length=50)
    team= models.ForeignKey(Teams,on_delete=models.CASCADE, null=True, blank=True)