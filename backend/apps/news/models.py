from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    title        = models.CharField(max_length=255)
    slug         = models.SlugField()
    content      = models.TextField()

    is_published = models.BooleanField()

    entered_by   = models.ForeignKey(User)
    entered_on   = models.DateTimeField(auto_now_add=True)
