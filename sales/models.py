from django.db import models

from books.models import Book #because we need to connect sales with books

class Sale(models.Model):
    class Meta:
        db_table = 'sales'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # Number of books sold 
    quantity = models.PositiveIntegerField()

    # Total sale price
    price = models.FloatField()

    #Date of sale - will be automatically set to the current date.
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}"
    
