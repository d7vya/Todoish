from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from home.models import *
from home.forms import *
from django.db.models import Count, Q
import random
import string

def TeamCode():
    chars=string.ascii_letters
    l=8
    return ''.join(random.choice(chars) for _ in range(l))


# Create your views here.
@login_required(login_url='/auth/login')
def homepage(request):
    usertask=Tasks.objects.filter(assigned_to=request.user )and Tasks.objects.filter(assigned_by=request.user)
    
    return render(request,'homepage.html',{'usertask':usertask})

def createtask(request):
    form= UserTaskForm()
    if request.method=="POST":
        form=UserTaskForm(request.POST)
        if form.is_valid():
            task=Tasks.objects.create(assigned_by=request.user)
            task.assigned_to.set([request.user])
            form=UserTaskForm(request.POST, instance=task)
            form.save()
            return redirect('/')

    return render(request,'createtask.html',{'form':form})

def jointeam(request,teamcode):
    team=Teams.objects.get(code=teamcode)
    context={}

    context={'team':team}
    if request.user not in team.members.all():
        context['message']='Join The Team '
    else:
        context['msg']='you are already in the team'
    if request.method=='POST':
        if request.user not in team.members.all():
            
            team.members.add(request.user)
            return redirect('/team')
    return render(request,'teamjoin.html',context)  
 




def manageteam(request):
    teamcode=request.GET.get('teamcode','')
    if teamcode:
        return jointeam(request,teamcode)
        
    form=TeamForm()
    if request.method=='POST':
        form=TeamForm(request.POST)
        if form.is_valid():

            team=Teams.objects.create(owner=request.user,name=form.cleaned_data['name'])
            while True:
                teamcode=TeamCode()
                if not Teams.objects.filter(code=teamcode).exists():
                    break
            team.code=teamcode
            team.admins.set([request.user])
            team.members.set([request.user]) 
            team.save()   
            return redirect(f'/teaminfo?team={teamcode}')
    teams=userteams(request.user)
    return render(request,'teammanage.html',{'form':form,'teams':teams})


def teaminfo(request):
    teamcode= request.GET.get('team')
    team=Teams.objects.get(code=teamcode)
    if team:
        domain = request.get_host()
        link=f'{domain}/teams/{team.code}'
        
        teams=userteams(request.user)
        return render(request,'teammanage.html',{'link':link,'curteam':team,'teams':teams})
    

def userteams(user):
    teams=user.userteam.all()
    return teams 

def tasklist(request):
    tasks=request.user.usertask.all()
    return render(request,'tasklist.html',{'list':tasks})