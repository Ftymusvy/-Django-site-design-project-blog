from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect


def register(request):

 if request.method == 'POST':
    #register user
    print('yes it is POST method')
    messages.error(request, 'this is atest for error message.')
    return redirect('register')  
 else: 
    return render(request , 'accounts/register.html')

def login(request):

 if request.method == 'POST':
    # login user
    pass 
 else:   
    return render(request , 'accounts/login.html')

def logout(request):
    return redirect('index')