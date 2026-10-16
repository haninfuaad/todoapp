from django.db import models

# Create your models here.
class Lead(models.Model):
    SOURSE_CHOICE=(
        ("walk in","walk in"),
        ("referral","referral"),
        ("website","website")
    )
    STATUS_CHOICE=(
        ("new","new"),
        ("contacted","contacted"),
        ("converted","converted"),
        ("lost","lost")
    )
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=40,unique=True)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=40)
    sourse=models.CharField(max_length=40,choices=SOURSE_CHOICE)
    status=models.CharField(max_length=50,choices=STATUS_CHOICE)
    added_date=models.DateTimeField(auto_now=True)
    notes=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.name}-{self.phone}"