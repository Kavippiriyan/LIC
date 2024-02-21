from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower


# Restaurent
# User
# Rating

# custom validators
def Restaurent_name_should_starts_with_I(self):
    if not self.startswith('I'):
        raise ValidationError("Restaurent name must begin with I")

class Restaurent(models.Model):
    class Typechoices (models.TextChoices):
        INDIAN = 'IN','INDIAN'
        CHINESE = 'CH','CHINESE'
        ITALIAN = 'IT', 'ITALIAN'
        GREEL = 'GR', 'GREEK'
        MEXICAN = 'MX', 'MEXICAN'        
        FASTFOOD = 'FF','FASTFOOD'
        OTHER = 'OT', 'OTHER'

    name = models.CharField(max_length=50, validators = [Restaurent_name_should_starts_with_I])
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField(validators = [MinValueValidator(-90),MaxValueValidator(90)])
    logitude = models.FloatField(validators = [MinValueValidator(-180),MaxValueValidator(180)])
    Restaurent_type = models.CharField(max_length=2, choices=Typechoices.choices )


    # class Meta:
    #     ordering = [Lower('name')]
    #     get_latest_by = 'date_opened'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='filter_users')#on_delete=models.CASCADE, we are delete id=1 the respective id of details will be delete
    Restaurent =models.ForeignKey(Restaurent, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
    validators = [MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return f"Rating :{self.rating}"
    
class Sale(models.Model):
    Restaurent = models.ForeignKey(Restaurent, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Sale: {self.income} at {self.time.strftime('%Y-%m-%d %H:%M:%S')}"
   

