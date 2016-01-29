from django.db import models

# Create your models here.

class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)

    def json(self):
        return {
            'id': self.id,
            'title': self.title
        }