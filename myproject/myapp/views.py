from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def index(request):
    return render(request, 'pages/index.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Votre message a bien été envoyé.")
            return redirect('contact')  # Rediriger vers la même page après soumission

    return render(request, 'pages/contact.html')
def message_list(request):
    # Récupérer tous les messages
    messages = ContactMessage.objects.all()
    return render(request, 'admin/message.html', {'messages': messages})