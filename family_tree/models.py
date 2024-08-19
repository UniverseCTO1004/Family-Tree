from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()

class FamilyMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

class Relationship(models.Model):
    parent = models.ForeignKey(FamilyMember, related_name='children', on_delete=models.CASCADE)
    child = models.ForeignKey(FamilyMember, related_name='parents', on_delete=models.CASCADE)
