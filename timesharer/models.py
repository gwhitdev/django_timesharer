from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
class Organisation(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    is_live = models.BooleanField()
    tags = TaggableManager()
    created_at = models.DateTimeField('date created')
    def __str__(self):
        return self.name

class Volunteer(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    opted_in = models.BooleanField(default=False)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    is_live = models.BooleanField()
    #applied_to = models.OneToMany(Opportunity, on_delete=models.CASCADE, default="1")
    tags = TaggableManager()
    def __str__(self):
        return self.name

class Opportunity(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(default='Description')
    is_live = models.BooleanField()
    owned_by = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    volunteers = models.ForeignKey(Volunteer, on_delete=models.CASCADE, default=3)
    tags = TaggableManager()
    created_at = models.DateTimeField('date created',default=timezone.now)
    def __str__(self):
        return self.title
