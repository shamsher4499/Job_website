from django.db import models

CHOICES = ((1,'Full-time'),(2,'Part-time'),(3,'Internship'))
class Job(models.Model):
    title = models.CharField(max_length=50)
    exp = models.CharField(max_length=20)
    type = models.IntegerField(choices=CHOICES, default=1)
    url = models.CharField(max_length=300)
    created_at = models.DateTimeField()
    company = models.CharField(max_length=50)
    # company_url = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50)
    # description = models.TextField()
    # how_to_apply = models.TextField()
    company_logo = models.ImageField(upload_to="myimage")
    salary = models.CharField(max_length=20)

    def __str__(self):
        return self.title
