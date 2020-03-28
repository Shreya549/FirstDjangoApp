from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                print('Username exists')
                cond1 = True
        
        if (password1!=password2):
            messages.info(request, 'Password not matching')
            print('Password not matching')
            cond2 = True
        
        if (cond1 or cond2):
            return render(request, 'register.html')

        if (not cond1 and not cond2):
            user = User.objects.create_user(
                username = username, 
                password = password1, 
                email = email, 
                first_name = first_name, 
                last_name = last_name
            )
            user.save()
            print('User created')
            return redirect('login')
        
        
    else:
        return render(request, 'register.html')
        

def login(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if (user is not None):
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Credentials incorrect")
            return redirect('login')


    else:
        return render(request, 'login.html')