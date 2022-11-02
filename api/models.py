from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    id = models.CharField(unique=True, default=uuid.uuid4, primary_key=True, max_length=36, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    famous = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Publisher(BaseModel):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(BaseModel):
    name = models.CharField(max_length=255)
    pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="book")
    
    def __str__(self):
        return self.name
