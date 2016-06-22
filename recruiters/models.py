from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Applicants(models.Model):
    # user = models.ForeignKey(User)
    resume = models.BooleanField(default=False)
    candidate_name = models.CharField(max_length=250)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=100)
    experience = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, editable=False)
    current_location = models.CharField(max_length=100)
    preferred_location = models.CharField(max_length=100)
    expected_ctc = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, editable=False)
    current_employer = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)
    skills = models.CharField(max_length=500)
