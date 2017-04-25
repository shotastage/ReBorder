from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_student_id = models.CharField(max_length=8)
    user_ethereum_account = models.CharField(max_length=100)
    user_is_admin = models.BooleanField



class GameSession(models.Model):
    session_id = models.CharField(max_length=100)
    isEnable = models.BooleanField
    isRevoked = models.BooleanField
