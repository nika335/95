from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    date_created = models.CharField(max_length=20)
    

    def __str__(self):
        return self.title
