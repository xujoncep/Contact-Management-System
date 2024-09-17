from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'delete_contact.html', {'contact': contact})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})

def search_contacts(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(email__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})
