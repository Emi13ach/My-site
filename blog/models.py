from django.db import models
from django.urls import reverse
from datetime import date


class Tag(models.Model):
    caption = models.CharField(max_length=80)
    
    def __str__(self):
        return str(self.caption)
    
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, e-mail: {self.email}"
    

class Post(models.Model):
    title = models.CharField(max_length=254)
    excerpt = models.CharField(max_length=254)
    image_name = models.CharField(max_length=80)
    date = models.DateField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
        
    def __str__(self):
        return f"{self.title}"
    
    
    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])

