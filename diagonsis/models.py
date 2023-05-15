from django.db import models
from accounts.models import CustomUser
# Create your models here.
def image_upload(instance, filename):
    try:
        image_name, extension = filename.split(".")
        return "tests/%s/%s.%s" % (instance.user, image_name, extension)
    except ValueError:
        raise ValueError("Invalid file format. Please make sure to upload a file with an extension.")
class MedicalTest(models.Model):
    test_types = (
        ("anemia", "أنيميا"),
        ("anemia-hada", "أنيميا حادة "),)
    # test_type=models.CharField(max_length=50, choices=test_types, default="anemia")
    user=models.ForeignKey( CustomUser,on_delete=models.CASCADE)
    # title=models.CharField( max_length=30) 
    image=models.ImageField( upload_to=image_upload, height_field=None, width_field=None, max_length=None)
    upload_date=models.DateTimeField( auto_now=True)
    result = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return ( str(self.upload_date) )