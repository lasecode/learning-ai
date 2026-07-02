from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contacts


# Create your views here.
def create_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return HttpResponse("Invalid Form")
    else:
        form = ContactForm()
    
    return render(request, 'create_contact.html', {'form':form})

def view_contacts(request):
    query = Contacts.objects.all()
    return render(request, 'template.html', {'contacts': query})


def delete_contact(request,pk):
    contact = Contacts.objects.get(pk=pk)

    if request.method == "POST":
        contact.delete()
        return redirect('home')
    else:
        return render(request, 'delete_confirm.html', {'contact': contact})


def update_contact(request, pk):
    contact = Contacts.objects.get(pk=pk)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm(instance=contact)
    return render(request, 'update_contact.html', {'form':form})

    
        
def search_contacts(request):
    query = request.GET.get('name')
    results = Contacts.objects.filter(name__icontains=query)
    return render(request, 'search_contacts.html', {'results':results})
