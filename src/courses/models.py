from django.db import models


class PublishedStatus(models.TextChoices):
    PUBLISHED = "PU", "Published"
    DRAFT = "DR", "Draft"
    COMMING_SOON = "CS", "Comming Soon"


class AccessStatus(models.TextChoices):
    ANYONE = "AN", "Anyone"
    EMAIL_REQUIRED = "ER", "Email Required"


# Create your models here.
class Courses(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/", null=True, blank=True)
    access = models.CharField(
        max_length=120, choices=AccessStatus.choices, default=AccessStatus.ANYONE
    )
    status = models.CharField(
        max_length=120, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT
    )

    @property
    def is_published(self):
        return self.status == PublishedStatus.PUBLISHED

    def __str__(self):
        return self.title
