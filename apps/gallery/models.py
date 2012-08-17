from datetime import datetime
from django.db import models


class PhotoUrl(models.Model):
    url = models.CharField(max_length=128)
    uploaded = models.DateTimeField()
    
    def save(self):
        self.uploaded = datetime.now()
        models.Model.save(self)