from django.db import models

class person(models.Model):
    fullname = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    bankbalance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    isstudent = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname