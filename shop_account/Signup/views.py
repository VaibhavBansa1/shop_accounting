from django.shortcuts import render

# Create your views here.
def sign_up(request):
    return render(request, 'sign_up.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def firm_register(request):
    return render(request, 'firm_register.html')

def forgot(request):
    return render(request, 'forgot.html')

def forgot_pass(request):
    return render(request, 'forgot_pass.html')