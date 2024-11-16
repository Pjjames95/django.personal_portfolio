### PORTFOLIO PROJECT.
## PROJECT DETAILS
Project name - Personal_portfolio
App_name - port_folio
Contents in the app:
   -migrations
   -static(images and global stylesheet)
    -templates(templates)
    -all the other utilities that comes with django app once its started
    -accompanied by this README file.

### FRONTEND
On this section there was full utilisation of HTML and CSS with the inclusion of the Bootstrap framework.
The section comprises of the landing page which contains a navigation bar with buttons to navigate to the other web pages, 
it also contains my information in terms of introduction, my skills and hobbies as well as my professional background and the last part
is the footer part that comprises of my contact details. 
The 'about' takes the user down to the section with my professional background.
The navigation part has a button to navigate to the section where a person can leave me with a message and has its own validation where
the user must fill all the blanks in the form before submitting as well as write in a message that does not lessen 100 characters. More
of the other HTML templates I will explain in my views.py.
The other crucial html template is myproject that the user can reach to by pressing the projects part on the navigation part.
About the CSS, utilisation of different types of css were used i.e inline, internal as well as an external css stylesheet.
I also included social media icons form the bootstrap framework at the footer which contains my information.
# Custom CSS Styles for port_folio

This repository contains custom CSS styles for enhancing the visual appeal of your portfolio website. The styles include responsive design, message styling, and interactive elements.

## Description

The CSS styles provided in this project cover a variety of visual enhancements, including:
- Container styling with a semi-transparent background and shadow.
- Custom message styling for success, error, and warning messages.
- Hover effects for buttons.
- Customized navbar styling with a unique color scheme.


### BACKEND
## Models(Django Contacts Model)
This repository contains the Django model `Contacts` for managing contact information,
along with custom validation to ensure message length.
The `Contacts` model is designed to store and manage contact details, including name, email, phone number, and message. 
The model includes custom validation to ensure that messages are at least 100 characters long.

## Views.py(Django Views for Contact Management)

This repository contains Django view functions for managing contacts, including 
-creating, 
-listing, 
-updating, and 
-deleting contact information. 
These views are designed to work with the `Contacts` model.

## Description

The provided Django view functions handle various operations related to contact management:
- Displaying a portfolio page(landing page)
- Listing all contacts
- Creating a new contact
- Deleting a contact
- Updating a contact
- Displaying a projects page
# Messages
Imported from the django.contrib and this is how thy function on completion of an operation.
Success Message: Indicates a successful operation.
Error Message: Indicates an error occurred during an operation


# urls.py (Django URL Configurations for Contact Management)

This repository contains the URL configurations for a Django project, mapping various endpoints to their respective view functions. 
These URLs handle operations such as displaying a portfolio page, managing contacts, and listing projects.

## Description

The URL configurations provided in this project handle various operations related to contact management and other pages:
- Displaying a portfolio page(landing page)
- Listing all contacts
- Creating a new contact
- Deleting a contact
- Updating a contact
- Displaying a projects page
## STATICFILES
This are the files like CSS, JavaScript, and images that are not dynamically generated and are served as-is to the client’s browser.
Managing static files correctly is essential for a smooth user experience and improved performance.
Steps to add static files:
- create a directory by the name " static " on the app directory and in it create a directory for css and another one for images.
- On your settings we must make sure the static settings are configured this way:
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
- with the root being static files
- after that we use this command to collect all our static files 
[ python manage.py collectfiles ]
- then take option [ yes ] to give permission for the collection of our files and it gives us a notification that files have been
copied to a certain path.
The css in this directory becomes our global styling sheet for all our templates and the content in other files which is the same
with our images and can be used in any html template.

### CLARIFIER
Any other information concerning the project is written inside the different files where I deemed it right and appropriate to 
include it. Thanks for reading this README file.











    