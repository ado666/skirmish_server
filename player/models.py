from django.db import models

# Create your models here.

class Player(models.Model):
    id = models.AutoField(primary_key=True)

    login       = models.CharField(max_length=50)
    password    = models.CharField(max_length=50)
    status      = models.IntegerField()

    hash        = models.CharField(max_length=50)
    push_id     = models.CharField(max_length=100)

    def json(self):
        return {
            "userId": self.id,
            "login": self.login,
            "status": self.status,
        }