from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class messageModel(models.Model):
    from_user = models.ForeignKey(User,related_name='from_user',on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)
    message=models.CharField(max_length=1000)
    time_sent=models.DateTimeField(default=timezone.now)

    def opened(self):
        self.open=True
        self.save()

class taskModel(models.Model):
    assigned_to = models.ForeignKey(User,related_name='assigned_to',on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User,related_name='assigned_by',on_delete=models.CASCADE)
    task=models.CharField(max_length=1000)
    mark_as_done=models.BooleanField(default=False)

    def marked(self):
        self.mark_as_done = True
        self.save()