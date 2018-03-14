from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=50)
    File = models.FileField(upload_to="uploaded file")

    def __str__(self):
        return self.name
    
    class Meta:
        db_tabel = "uploaded file"