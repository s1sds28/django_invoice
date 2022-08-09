### Project title:
Django Invoice Application

### Project Description:
Application to create a simple invoices. This application allows full CRUD
functionality relating to invoices in the Django REST framework.

##### Reason for building
I wanted this application for myself. Many book-keeping and invoice software programs come with too many accessories. I wanted to create and store my own invoices.   
I only need to write a few invoices a month, so this is perfect for me and my personal use.

### How it works for me
I can use the django application to easily create and store invoices with a simple naming convention <title><month><year> for the title and other basic information for record keeping purposes. If I want to print or email a specific invoice I use the
action: export invoicesPDF.

### Installation
From terminal
mkdir invoice_application
cd invoice_application
git clone XXX
###### To create a virtual environment
virtualenv env
###### To activate virtual environment
source env/bin/activate
cd django_invoice
###### Install requirements
pip install - r requirements.txt
###### Run program
python manage.py runserver
###### Login
username: admin
password: testpass123
###### Use the appliction
Use the link from API root localhost:8000/admin/ to use the application
