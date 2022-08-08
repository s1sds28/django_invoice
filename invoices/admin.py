# invoices/admin.py
from django.contrib import admin
from . models import Invoice

import decimal, csv

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['created', 'owner', 'title', 'bill_to', 'bill_from',
    'line_item', 'monetary_value']

    def export_invoicesCSV(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="invoices.csv"'
        writer = csv.writer(response)
        writer.writerow(['Created', 'Owner', 'Title', 'Bill to', 'Bill From',
        'Line Items', 'Monetary Value'])
        invoices = queryset.values_list('created', 'owner', 'title', 'bill_to',
        'bill_from', 'line_item', 'monetary_value')
        for invoice in invoices:
            writer.writerow(invoice)
        return response
    export_invoicesCSV.short_description = 'Export InvoicesCSV'

    def export_invoicesPDF(modeladmin, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        writer = csv.writer(response)
        template_path = 'invoices/pdf1.html'

        invoices = queryset.values_list('created', 'owner', 'title', 'bill_to',
        'bill_from', 'line_item', 'monetary_value')
        info_list = []
        for invoice_item in invoices:
            info_list.append(invoice_item)
        info_list = info_list[0]

        #bill to
        bill_to = queryset.values('bill_to')
        bill_to = bill_to[0].get('bill_to')

        #bill from
        bill_from = queryset.values('bill_from')
        bill_from = bill_from[0].get('bill_from')

        #line item
        line_item = queryset.values('line_item')
        line_item = line_item[0].get('line_item')

        #monetary_value
        monetary_value = queryset.values('monetary_value')
        monetary_value = monetary_value[0].get('monetary_value')

        #title
        title = queryset.values('title')
        title = title[0].get('title')

        # Create a Django response object, and specify content_type as pdf
        context = {'info_list': info_list, 'bill_to': bill_to,
        'bill_from': bill_from, 'line_item': line_item, 'monetary_value':
        monetary_value, 'title': title}

        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
           html, dest=response)
        return response

    export_invoicesPDF.short_description = 'Export InvoicesPDF'

    actions = [export_invoicesCSV, export_invoicesPDF]

admin.site.register(Invoice, InvoiceAdmin)
