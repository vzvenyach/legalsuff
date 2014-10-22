from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField
from django.core.urlresolvers import reverse

# Create your models here.

class Sufficiency(models.Model):
    STATUS = Choices('draft', 'published')
    status = StatusField()
    COUNCILMEMBERS = Choices("Chairman Phil Mendelson", "Councilmember Yvette Alexander")
    councilmember = models.CharField(choices=COUNCILMEMBERS, max_length=60, default="Chairman Phil Mendelson")
    measure_type = models.CharField(choices=Choices("Bill", "Proposed Resolution"), max_length=30, default="Bill")
    measure_number = models.CharField(max_length=15)
    short_title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.measure_type + " " + self.measure_number

    def get_absolute_url(self):
        return reverse('show_sufficiency', kwargs={'sufficiency_id': self.pk})