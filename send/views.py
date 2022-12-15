from django.shortcuts import render
from django.core.mail import send_mail
def index(request):
    send_mail('hello this is subject','hello this is body','srirangarajuvadali@gmail.com',['sriranga451@gmail.com'],fail_silently=False)
    return render(request,'send/index.html')
