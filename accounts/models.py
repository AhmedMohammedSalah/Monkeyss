from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission



def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "labs/%s/%s.%s" % (instance.username, instance.username, extension)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_doctor = models.BooleanField(default=False)
    is_admmin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_upload, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    address =models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    verify_image=models.BooleanField(default=False)
    rate1=models.BooleanField(default=False)
    rate2=models.BooleanField(default=False)
    rate3=models.BooleanField(default=False)
    rate4=models.BooleanField(default=False)
    rate5=models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)
    def __str__(self):
        return self.email
    