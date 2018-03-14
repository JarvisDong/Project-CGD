from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'picture')


    def __str__(self):
        return self.name

    class Meta:
        db_table = "picture"
