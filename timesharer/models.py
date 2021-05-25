from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Organisation(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    is_live = models.BooleanField()
    tags = TaggableManager()
    def __str__(self):
        return self.name

class Opportunity(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(default='Description')
    #labels = models.
    is_live = models.BooleanField()
    owned_by = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    tags = TaggableManager()
    def __str__(self):
        return self.title

class Volunteer(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    #username = models.CharField(max_length=20)
    opted_in = models.BooleanField(default='false')
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    is_live = models.BooleanField()
    applied_to = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    tags = TaggableManager()
    def __str__(self):
        return self.name




    
    
