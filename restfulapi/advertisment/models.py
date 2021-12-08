from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Advertisment(models.Model):

    website_url = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.PositiveIntegerField()
    title = models.TextField(max_length=80)
    photo_url = models.URLField()
    transaction_number = models.TextField(max_length=12)
