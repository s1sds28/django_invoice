# invoices/views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Invoice
from .permissions import IsOwnerOrReadOnly
from .serializer import InvoiceSerializer, UserSerializer

class InvoiceHighlight(generics.GenericAPIView):
    queryset = Invoice.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        invoice = self.get_object()
        return Response(invoice.highlighted)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'swagger link': 'http://127.0.0.1:8000/docs',
        'admin_link': 'http://127.0.0.1:8000/admin/',
        'users': reverse('user-list', request=request, format=format),
        'invoices': reverse('invoice-list', request=request, format=format)
    })

class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
