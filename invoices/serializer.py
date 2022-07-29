# invoices/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from invoices.models import Invoice, LANGUAGE_CHOICES, STYLE_CHOICES


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='invoice-highlight', format='html')

    class Meta:
        model = Invoice
        fields = ('url', 'id', 'created', 'title', 'owner', 'bill_to', 'bill_from',
        'line_item', 'monetary_value')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # invoices = serializers.HyperlinkedRelatedField(
    #     many=True, view_name='invoice-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username')
