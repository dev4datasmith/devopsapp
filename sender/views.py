from django.shortcuts import render
from .utils import send_email

# Create your views here.
from django.http import HttpResponse


def index(request):
     if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_list = [request.POST.get('recipient_email')]

        send_email(subject, message,  recipient_list)

        # You can add additional logic or redirection after sending the email
        return render(request, 'success.html')
  

     return render(request, "sender.html")
