# Create your views here.
from django.views.generic.edit import CreateView
from .models import ContactMessage

class ContactFormView(CreateView):
    template_name = 'contact.html'
    model = ContactMessage
    fields = ["name", "email", "message"]
    success_url = "/contact"

