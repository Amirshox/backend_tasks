from django.db import models


class Staff(models.Model):
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField()
    salary = models.DecimalField(decimal_places=2, max_digits=15)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['birth_date']
