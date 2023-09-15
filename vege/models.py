from django.db import models

# Create your models here.
class receipi(models.Model):
    receipi_name = models.CharField(max_length=50)
    receipi_desc = models.CharField(max_length=500)
    reci_img = models.FileField(upload_to='receipi', max_length=100)

    def __str__(self): 
        return self.receipi_name