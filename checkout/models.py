from django.db import models
from products.models import Product

# Create your models here.
# models are what you are going to put in the database. This is all the information that you might require from a customer.

# import product model
# blank= false means it cannot be left blank

class Order(models.Model):
  full_name = models.CharField(max_length=50, blank=False)
  phone_number = models.CharField(max_length=20, blank=False)
  country = models.CharField(max_length=40, blank=False)
  postcode = models.CharField(max_length=20, blank=True)
  town_or_city = models.CharField(max_length=40, blank=False)
  street_address1 = models.CharField(max_length=40, blank=False)
  street_address2 = models.CharField(max_length=40, blank=False)
  county = models.CharField(max_length=40, blank=False)
  date = models.DateField()

  def __str__(self):
    return '{0}-{1}-{2}'.format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False)
  product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)
  quantity = models.IntegerField(blank=False)

  # we can return this as a string as follows:

  def __str__(self):
    return '{0} {1} @ {2}'.format(self.quantity, self.product.name, self.product.price)





