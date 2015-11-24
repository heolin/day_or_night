from django.db import models
from django.utils import timezone

class Document(models.Model):
    docfile = models.ImageField(upload_to='documents/%Y/%m/%d')
    source = models.CharField(max_length=200, default="")
    day_score = models.FloatField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

class DocumentClassification(models.Model):
    document = models.ForeignKey(Document)
    score = models.FloatField(default=0)
    ip = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
