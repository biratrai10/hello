from django.db import models
from django.core import validators
from .validators import validate_number
from PIL import Image
# Create your models here.
class CompanyHeader(models.Model):
        title = models.CharField(max_length=200)
        image = models.ImageField(upload_to='blog/', null=True)
        address= models.CharField(max_length=100)
        email1= models.EmailField()
        email2= models.EmailField()
        phone1=models.CharField(max_length=10)
        phone2=models.CharField(max_length=10)
        contact_image= models.ImageField(upload_to='blog/', null=True)
        google_embed=models.CharField(max_length=500,null=True)
        is_active = models.BooleanField(default=True,unique=True,null=True)    

        def __str__(self):       
            return self.title

        # def save(self):
        #     super().save()

        #     img=Image.open(self.contact_image.path)

        #     if img.height>466 or img.width>2442:
        #         output_size=(466,2442)
        #         img.thumbnail(output_size)
        #         img.save(self.contact_image.path)

class ContactInfo(models.Model):
        name=models.CharField(max_length=200)
        email=models.EmailField()
        phone=models.CharField(max_length=10,null=True, validators=[validate_number])
        subject=models.CharField(max_length=100, null=True)
        message=models.TextField(null=True,blank=True)
        
        def __str__(self):       
            return self.name