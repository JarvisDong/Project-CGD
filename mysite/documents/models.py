import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

'''
class uploaded(models.Model):
    doc_name = models.CharField(max_length=200)
    category = models.CharField(max_length = 50, blank = True)
    pub_date = models.DateTimeField(auto_now=False)

    class Meta:
        db_table = "newdoc"

    def was_published_recently(self):
        now = timezone.now()	
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"
    
    def __str__(self):
        return self.doc_name


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

'''


class newdoc(models.Model):
    #category = models.ForeignKey(Category)
    #tags = models.ManyToManyField(Tag, blank=True)
    #excerpt = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    def __str__(self):
        return self.title


