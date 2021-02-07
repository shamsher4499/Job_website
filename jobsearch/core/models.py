from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=50)
    exp = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    company_url = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50)
    description = models.TextField()
    how_to_apply = models.TextField()
    company_logo = models.ImageField(upload_to="myimage")

    def __str__(self):
        return self.title
