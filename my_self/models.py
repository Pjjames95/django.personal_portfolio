from django.core.exceptions import ValidationError
from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=15, null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.name

    def clean(self): #sets the number of characters in the field to a minimum of 100 characters and if its validated,
        #a validation message is displayed to warn the user of the later.
        super().clean()
        if len(self.message) < 100:
            raise ValidationError("Message must be at least 100 characters long.")



