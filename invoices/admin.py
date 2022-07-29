# invoices/admin.py
from django.contrib import admin
from . models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    pass
    # readonly_fields = ('highlighted',)

admin.site.register(Invoice, InvoiceAdmin)
