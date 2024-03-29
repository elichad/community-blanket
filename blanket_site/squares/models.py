from django.db import models
from django.urls import reverse

from contributors.models import Person, get_anonymous_user


class Square(models.Model):
    """Model for tracking individual contributions."""

    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    creator = models.ForeignKey(Person, on_delete=models.SET(get_anonymous_user))
    date_created = models.DateField()
    date_time_uploaded = models.DateTimeField(db_default=models.functions.Now())
    description = models.TextField()
    notes = models.TextField(blank=True)

    # TODO: fields relating to location in a larger blanket

    def get_absolute_url(self):
        return reverse("squares:square-detail", kwargs={"pk": self.pk})
