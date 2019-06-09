from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    info_box = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Free(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    info_box = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Tip(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    info_box = models.BooleanField(default=True)

    def __str__(self):
        return self.title