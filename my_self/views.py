from django.contrib import messages #to help in displaying success and warning messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactsForm
from .models import Contacts


def portfolio(request): #displays the landing page
    return render(request, 'my_self/Portfolio.html')



def contacts_lister(request): #this one will display the contact lister and take all the ojects in the models
    contacts = Contacts.objects.all()
    return render(request, 'my_self/contacts_lister.html', {'contacts': contacts})

def contact_create(request): #responsible for the creation of a new user's contacts as well as the message
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save() #validation of the form
            messages.success(request, 'Your information has successfully been created! Thanks for checking out on me!') #if the user has filled in information in the
            #correct form as stated, then this message is displayed to congratulate them.
            return redirect('contacts_lister')
        else: #the user is given a message to alert them of an error that occurred during their data entry
            messages.error(request, 'There was an error creating the contact. Check your contact info and the message, if its less than 100 characters then, PLEASE TRY AGAIN.')
    else:
        form = ContactsForm()
    return render(request, 'my_self/contacts_form.html', {'form': form})

def del_contact(request,pk): #operation responsible for deleting contacts information
    contact = get_object_or_404(Contacts, pk=pk)
    if request.method == "POST":
        contact.delete() #confirms the pk displayed if its available for deletion or not and displays a message on completion
        messages.success(request, 'Your information has successfully been deleted!')
        return redirect('contacts_lister')
    #we have to confirm if the user really intends to delete their message or not
    return render(request, "my_self/confirm_delete.html", {'contact': contact})

def update_contact(request,pk): #operation for updating the user's information
    contact = get_object_or_404(Contacts, pk=pk)
    if request.method == "POST":
        form = ContactsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save() #form validation for the update and returns a message that the information has successfully been updated
            messages.success(request, 'Your information has successfully been updated!')
            return redirect('contacts_lister')
    else:
        form = ContactsForm(instance=contact) #if the form is not valid, it returns the user back to the contacts form.
        return render(request, 'my_self/contacts_form.html', {'form': form})

def my_projects(request): #an operation for displaying the projects webpage.
    return render(request, 'my_self/myprojects.html')







