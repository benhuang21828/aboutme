from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    start = models.DateField(default=datetime.now())
    end = models.DateField(null=True,blank=True)
    content = models.TextField(null=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return u"{}".format(self.title)

class Bio(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    about = models.TextField(max_length=200, null=True)
    owner = models.OneToOneField(User, primary_key=True)

    def __unicode__(self):
        return u"{}".format(self.name)


