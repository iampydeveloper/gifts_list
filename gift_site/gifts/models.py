# gifts/models.py
from django.db import models

class Gift(models.Model):
    link_name = models.CharField(max_length=100, unique=True)
    gift_text = models.TextField(blank=True, null=True)
    gift_link = models.URLField(blank=True, null=True)
    gift_image = models.ImageField(upload_to='gift_images/', blank=True, null=True)

    def __str__(self):
        return self.link_name

class GiftItem(models.Model):
    gift = models.ForeignKey(Gift, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='gift_images/', blank=True, null=True)

    def __str__(self):
        return self.name or "Unnamed Gift"