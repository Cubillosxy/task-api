from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} - {}'.format(self.description, self.user.username if self.user else '')

    class Meta:
        ordering = ['-id']