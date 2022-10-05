from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ("TAK", "TAK"),
    ("NIE", "NIE"),

)

class Form(models.Model):
    # Models
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.CharField(max_length=50, choices=CHOICES)
    title = models.CharField(max_length=200, blank=True, null=True)
    firstname = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    programmer_title = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    # ordering by time
    class Meta:
        ordering = ('-created',)

    # name by title
    def __str__(self):
        return self.title

class Area(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='areas')
    title = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
        

class Experience(models.Model):

    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='experiences')
    work_date = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    type_of = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    technology = models.CharField(max_length=200, blank=True, null=True)
    