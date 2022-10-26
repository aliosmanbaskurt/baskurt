from django.shortcuts import render,redirect


from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                password=password)
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    messages.info(request,'Geçersiz Kullancı')
        else:
            messages.info(request,'Şifrenizi veya adınızı kontrol ediniz')
    else:
        form=LoginForm()
    
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def dashboard (request):
    current_user =request.user
    return render(request,'dashboard.html')