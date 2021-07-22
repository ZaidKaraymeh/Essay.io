from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
class Essay(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title