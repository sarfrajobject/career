from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        request.session['username'] = username

        if user is not None:
            auth.login(request, user)
            return redirect('/')
           
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')
    else:
        return render(request, 'login.html')

def login(request):
   username = 'not logged in'
   
   if request.method == 'POST':
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         request.session['username'] = username
      else:
         MyLoginForm = LoginForm()
            
   return render(request, 'loggedin.html', {"username" : username})

def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'loggedin.html', {"username" : username})
   else:
      return render(request, 'login.html', {})           


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        em = request.POST['email']
        p_number = request.POST['phone_number']
        if password1 == password2:
            if User.objects.filter(username=user).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user, password=password1, email=em, first_name=first_name,
                                                last_name=last_name, phone_number=p_number)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching..')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
