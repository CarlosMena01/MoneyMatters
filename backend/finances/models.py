from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Transaction(models.Model):
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    amount = models.FloatField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.description