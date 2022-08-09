### Project title:
Django Invoice Application

### Project Description:
A Django application to create invoices. This application allows full CRUD
functionality relating to invoices in the Django REST framework.

### Reason for building
I wanted this application for myself. Many bookkeeping programs come with too many accessories. I wanted to create and store my own invoices.

### How it works for me
I can use the django application to easily create and store invoices with a simple naming convention in the title. If I want to print or email a specific invoice I use the admin
action: export invoicesPDF.

### Installation
From terminal

mkdir invoice_application

cd invoice_application

git clone https://github.com/s1sds28/django_invoice.git

###### To create a virtual environment
virtualenv env
###### To activate virtual environment
source env/bin/activate
###### change dir
cd django_invoice
###### Install requirements
pip install - r requirements.txt
###### make migrations
python manage.py makemigrations

python manage.py migrate
###### create user
python manage.py createsuperuser

-> enter username, email, and password when asked
###### Run program
python manage.py runserver
###### Use the application
Use the link from API root localhost:8000/admin/ to use the application
