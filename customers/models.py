from django.db import models

class Customer(models.Model):

    name= models.CharField(max_length=120)
    notes= models.TextField()
    pic = models.ImageField(upload_to='customers', default='no_picture.jpg')

    # customer name with ID = 1 will show the name (and not 1)
    def __str__(self):
        return str(self.name)
