from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

from manageuser.forms import RegisterForm,LoginForm
# Create your views here.
def loginuser(request):
    form = LoginForm()
    message = ''
    
    if request.method == 'POST':
        # Get the username and password from POST request
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        print(user)
        # If authentication is successful
        if user is not None:
            # Log the user in
         
            login(request, user)
            return redirect('/')
        else:
            # Invalid login
            message = 'Please enter correct username and password'
    
    return render(request, 'authuser.html', {'form': form, 'pagename': 'login', 'message': message})

def registeruser(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save to the database yet
            
            # Hash the password before saving the user
            user.set_password(user.password)
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            
            return redirect('/')
    return render(request,'authuser.html',{'form':form,'pagename':'register'})

def userlogout(request):
    logout(request)
    return redirect('/')

