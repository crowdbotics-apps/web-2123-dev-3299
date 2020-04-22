from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    fcfvz = models.OneToOneField(
        "home.CustomText",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_fcfvz",
    )
    ms = models.ManyToManyField("users.User", blank=True, related_name="customtext_ms",)
    sdfe = models.BigIntegerField(null=True, blank=True,)
    sfdf = models.ForeignKey(
        "home.DataModel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_sfdf",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class DataModel(models.Model):
    "Generated Model"
    abc = models.BigIntegerField()
    sdf = models.ManyToManyField(
        "home.CustomText", blank=True, related_name="datamodel_sdf",
    )
    cc = models.ManyToManyField(
        "home.CustomText", blank=True, related_name="datamodel_cc",
    )
