from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
'''
To do :
    -Owner
    -Title
    -content
    -Created_at
    -slug
'''
class Note(models.Model):
    owner = models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True , blank=True)
    
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)
