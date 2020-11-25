from django.db import models

# Create your models here.
class Service(models.Model):
    main_heading=models.CharField(max_length=200)
    main_background_image=models.ImageField(upload_to='service/',null=True)
    sub_heading=models.CharField(max_length=200)
    description = models.TextField(blank=True)

    box_image=models.ImageField(upload_to='service/',null=True)
    heading_title=models.CharField(max_length=20)
    description_title= models.TextField(blank=True)

    box_image1=models.ImageField(upload_to='service/',null=True)
    heading_title1=models.CharField(max_length=20)
    description_title1 = models.TextField(blank=True)

    box_image2=models.ImageField(upload_to='service/',null=True)
    heading_title2=models.CharField(max_length=20)
    description_title2 = models.TextField(blank=True)

    main_image=models.ImageField(upload_to='service/',null=True)

    sub_heading_title=models.CharField(max_length=20)
    sub_description_title = models.TextField(blank=True)

    sub_heading_title1=models.CharField(max_length=20)
    sub_description_title1 = models.TextField(blank=True)

    question=models.CharField(max_length=50)
    answer = models.TextField(blank=True)

    question1=models.CharField(max_length=50)
    answer1 = models.TextField(blank=True)

    question2=models.CharField(max_length=50)
    answer2 = models.TextField(blank=True)

    question3=models.CharField(max_length=50)
    answer3 = models.TextField(blank=True)

    question4=models.CharField(max_length=50)
    answer4 = models.TextField(blank=True)

    list_info=models.CharField(max_length=100)
    list_info1=models.CharField(max_length=100)

    def __str__(self):
        return self.main_heading








