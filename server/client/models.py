from django.utils import timezone
from django.db import models
import uuid
# Create your models here.


class client(models.Model):
    types = (
        ('water', '水系统'),
        ('wind', '通风系统'),
        ('TEST', 'TEST')
    )
    states = (
        ('online', '在线'),
        ('offline', '离线'),
        ('warning', '连接不稳定')
    )
    uuid = models.UUIDField(default=uuid.uuid1, editable=False, unique=True, primary_key=True)    
    group = models.CharField(max_length=32, choices=types, default='TEST')
    comment = models.CharField(max_length=50, default='', blank=True)
    state = models.BooleanField(default=True, editable=True)
    lastCommunication = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {} - {}".format(self.group, self.comment, self.uuid)


