from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PersonalInfo(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI')
    ]

    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image_data/')
    date_added = models.DateTimeField(default=timezone.now())
    type_of_chai = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='No Descriptions') #Text field is required that is why we set default=''.

    def __str__(self):
        return self.name
    
#one to many
class InfoReview(models.Model):
    info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user.username} review for {self.info.name}"
    

#Many to many
class Plateform(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    infos = models.ManyToManyField(PersonalInfo, related_name='plateform')

    def __str__(self):
        return self.name
    
#One to one
class InfoCertificate(models.Model):
    info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE, related_name='certificate')
    certifiacte_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now())
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for{self.info.name}'
    

# https://youtu.be/zUXhp3GkIqg?si=X8vCLArl7aQLiok3