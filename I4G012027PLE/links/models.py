from operator import mod
from pyexpat import model
from django.db import models
from .managers import ActiveLinkManager
from django.contrib.auth import get_user_model

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = get_user_model()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()

    public = ActiveLinkManager()
    
    def saveLink(self):
        self.target_url
        self.description
        self.identifier
        self.author
        self.created_date
        self.active
        self.save()

    def __str__(self) -> str:
        return self.description