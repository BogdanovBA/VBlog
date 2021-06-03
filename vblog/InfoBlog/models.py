from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    post_image = models.ImageField(upload_to="images/%Y/%m/d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)