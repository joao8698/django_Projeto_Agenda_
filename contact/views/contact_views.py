from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def inital_page(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[:10]

    return render(request,
                  'contact/index.html',
                  {
                      'contacts': contacts,
                  })