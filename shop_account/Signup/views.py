from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def signup(request):
    if request.method == 'POST':
        message = "Hello"
        email = request.POST.get('email')
        name = "Sivam"
        send_mail(
            'contact from',
            message,
            'settings.EMAIL_HOST_USER',
            [email], 
            fail_silently=False)
        return render(request, 'home.html')
    else:
        print("HAHAHA")
        
    return render(request, 'signup.html')
