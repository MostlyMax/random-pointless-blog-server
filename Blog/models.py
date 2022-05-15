from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=256, blank=True)

    submitted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feature(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)

    title = models.CharField(max_length=64)
    body = models.CharField(max_length=256, blank=True)

    featured_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
