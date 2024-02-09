from django.db import models

from django.contrib.auth.models import User #needed for OneToOneField


class Salesperson(models.Model):
    # OneToOne specifies that each username can only be connected to one salesperson
    username = models.OneToOneField(User, on_delete=models.CASCADE)     # `CASCADE` specifies that whenever the user with username is deleted, the complete profile of the salesperson will be also deleted.
    bio = models.TextField(default="no bio...")     # Text box with default statement: “no bio”
    pic = models.ImageField(upload_to='salespersons', default='no_picture.jpg')

    def __str__(self):
        return f"Profile of {self.username.username}"


