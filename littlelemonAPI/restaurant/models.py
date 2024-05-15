from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateField()
    time_slot = models.SmallIntegerField(default=10)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    description = models.TextField(max_length=1000, default="")

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
