from django.db import models
#import datetime

# Create your models here.
class Blog(models.Model):
    Name = models.CharField(max_length=50, blank=True)
    Text = models.TextField(max_length=300)
    Image = models.ImageField(upload_to='image/', default='a.png')
    Video = models.FileField(upload_to='video/', null=True, verbose_name='')
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = 'BlogData'


