### Project title:
Django Invoice Application

### Project Description:
A Django application to create invoices. This application allows full CRUD functionality relating to invoices in the Django REST framework.

### Reason for building
I wanted this application for myself. Many bookkeeping programs come with too many accessories. I wanted to create and store my own invoices.

### How it works for me
The application use case is to easily create, read, update, and delete invoices. If I want to download a specific invoice use the admin action: export invoicesPDF.

### Installation

Using python 3.8

From terminal

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
python manage.py migrate
###### python manage.py createsuperuser
-> create username, email, and password when asked
###### Run program
python manage.py runserver
###### Use the appliction
Use the link from API root localhost:8000/admin/
