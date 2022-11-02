
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedModel

class Enquiry(TimeStampedModel):
    name = models.CharField(_('Your Name'), max_length=100)
    phone_number = PhoneNumberField(_("Phone number"), max_length=30, default="+265998108842")
    email = models.EmailField(_('Email Address'))
    subject = models.CharField(_('Subject'), max_length=100)
    message = models.TextField(_('Message'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Enquiries"   