from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length= 50, blank=False)
    img = models.ImageField(upload_to='gallery', blank=True, null=True)
    content = models.TextField(null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True, db_index=True)\
    
