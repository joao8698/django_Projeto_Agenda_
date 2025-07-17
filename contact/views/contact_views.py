from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

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

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    return render(request,
                  'contact/contact.html',
                  {
                      'contact': single_contact,
                  })