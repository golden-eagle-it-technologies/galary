from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from autoslug import AutoSlugField


class Project(models.Model):
    name =models.CharField("Project Name", max_length=200)
    slug = AutoSlugField(populate_from='name')



class Version(models.Model):
    name =models.CharField("Version Name", max_length=200)
    slug = AutoSlugField(populate_from='name')
    project = models.ForeignKey(Project, related_name="versions", on_delete=models.CASCADE)




class Image(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(255, 140)],
                                      format='JPEG',
                                      options={'quality': 80})

    name =models.CharField("Page Name", max_length=200)
    version = models.ForeignKey(Version, related_name="images",on_delete=models.CASCADE)
