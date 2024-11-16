from django.urls import path
from .import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'), #landing page
    path('contact/contacts_lister', views.contacts_lister, name='contacts_lister'), #on navigation to contact it takes you to fill in contacts.
    path('contact/create',views.contact_create, name='contact_create' ), #directs the user to create their information
    path('contact/delete/<int:pk>',views.del_contact, name='del_contact'), #directs to the confirmation on deletion
    path('contact/update/<int:pk>',views.update_contact, name='update_contact'), #directs uers back to the contacts lister but with information to be updated.
    path('contact/my_projects', views.my_projects, name='my_projects'),
]
