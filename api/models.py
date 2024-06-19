from django.db import models
from helpers.models import TrackingModel
from authentication.models import User

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class ConditionColocation(models.Model):
    condition = models.TextField()
    
    def __str__(self) -> str:
        return self.condition
    
class Annonce(TrackingModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    location = models.CharField(max_length=255)
    conditions_colocations = models.ManyToManyField(ConditionColocation, null=True, blank=True, related_name='annonces')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
class AnnonceImage(models.Model):
    image = models.ImageField(upload_to=upload_to, blank=False, null=False)
    annonce = models.ForeignKey(to=Annonce, on_delete=models.CASCADE, related_name='images')
    
