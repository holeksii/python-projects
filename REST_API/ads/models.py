from django import db
from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from datetime import date

User = get_user_model()


class Advertisment(models.Model):
    transaction_number = models.CharField(
        verbose_name="Transaction_Number",
        db_index=True,
        unique=True,
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]{2}-[0-9]{3}-[a-zA-Z]{2}/[0-9]{2}$',
                message='Invalid format (should be: LL-NNN-LL/NN)',
            )
        ])

    website_url = models.URLField(verbose_name='Website_URL')
    photo_url = models.URLField(verbose_name='Photo_URL')
    start_date = models.DateField(verbose_name='Start_Date')
    end_date = models.DateField(verbose_name='End_Date')
    title = models.CharField(
        verbose_name='Title',
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]{2,}$',
                message='Only letters are allowed in title',
            )
    ])

    price = models.IntegerField(
        verbose_name='Price',
        validators=[MinValueValidator(limit_value=0, )],
    )

    user = models.ForeignKey(User,
                             verbose_name="User",
                             on_delete=models.CASCADE)
