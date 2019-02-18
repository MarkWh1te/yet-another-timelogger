from django.db import models
from django.contrib.auth.models import User
import time


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    action = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.duration = abs((self.end_time - self.start_time).total_seconds())
        super(Record, self).save(*args, **kwargs)

    def duration_time(self):
        return time.strftime('%H:%M:%S', time.gmtime(self.duration))

    def __repr__(self):
        return f'{self.action}:{self.start_time}'

    def __str__(self):
        return self.__repr__()

    class Meta:
        ordering = (
            '-end_time',
            'created',
        )
