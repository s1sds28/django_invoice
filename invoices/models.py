from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='invoice', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    bill_to = models.CharField(max_length=100, blank=True, default='')
    bill_from = models.CharField(max_length=100, blank=True, default='')
    line_item = models.CharField(max_length=100, blank=True, default='')
    monetary_value = models.PositiveIntegerField()

    class Meta:
        ordering = ['created']
