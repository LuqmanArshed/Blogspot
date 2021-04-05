from django.db import models

# Create your models here.



class Blog(models.Model):

    LATEST = 'latest'
    OLD = 'old'

    TECHNOLOGY = 'technology'
    SPORTS = 'sports'
    PAKISTAN = 'pakistan'
    INTERNATIONAL = 'international'
    URDU = 'urdu'
    ENGLISH = 'english'
    language_choices = [
        (URDU,'Urdu'),
        (ENGLISH,'English')
    ]

    category_choices = [

        (TECHNOLOGY,'Technology'),
        (SPORTS,'Sports'),
        (INTERNATIONAL,'International'),
        (PAKISTAN,'Pakistan')
    ]
    title = models.CharField(max_length=100,null=True,blank=True)
    blog_date = models.DateField(null=True,blank=True)
    header = models.TextField(null=True,blank=True)
    category = models.CharField(max_length=50,null=True,blank=True,choices=category_choices)
    language = models.CharField(max_length=50,null=True,blank=True,choices=language_choices)
    details = models.TextField(null=True,blank=True)
    thumbnail = models.ImageField(upload_to='BlogImages/',null=True,blank=True)
    title_image = models.ImageField(upload_to='BlogImages/',null=True,blank=True)
    center_image = models.ImageField(upload_to='BlogImages/',null=True,blank=True) 
    def __str__(self):
        return str(self.title)


     