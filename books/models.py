from django.db import models
from django.shortcuts import reverse

genre_choices= (
    ('classic', 'Classic'),
    ('romantic', 'Romantic'),
    ('comic', 'Comic'),
    ('fantasy', 'Fantasy'),
    ('horror', 'Horror'),
    ('educational', 'Educational'),
)
book_type_choices=(
    ('hardcover','Hard cover'),
    ('ebook', 'E-Book'),
    ('audiobook', 'Audiobook')
)
class Book(models.Model):

    name = models.CharField(max_length=120)
    author_name=models.CharField(max_length=100)
    pic = models.ImageField(upload_to='books', default='no_picture.jpg')
    genre = models.CharField(max_length=12, choices=genre_choices, default='cl')        # dropdown: Romance, classic, comic, fantasy, horror, other.
    book_type = models.CharField(max_length=12,choices=book_type_choices, default='hc')     #dropdown for booktype
    price = models.FloatField(help_text='in USdollars $')       # `help_text` allows to add a tooltip, which you will see below the form field in the admin panel
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
       return reverse ('books:detail', kwargs={'pk': self.pk})

    
