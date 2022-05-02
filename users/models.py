from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
	user_id = models.CharField(max_length=10, null=True)


class ImageUpload(models.Model):
	title = models.CharField(max_length=100, null=True)
	photo = models.ImageField(blank=True, upload_to=f"minwook", null=True)

	def __str__(self):
		return self.title
