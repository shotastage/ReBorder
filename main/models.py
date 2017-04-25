from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user_student_id = models.CharField(max_length=8)
    user_ethereum_account = models.CharField(max_length=100)
    user_is_admin = models.BooleanField
    user_is_completed_profile = models.BooleanField



class GameSession(models.Model):
    session_id = models.CharField(max_length=100)
    isEnable = models.BooleanField
    isRevoked = models.BooleanField



class SuperAdmin(models.Model):
    super_session_id = models.CharField(max_length=100)
    super_session_is_locked = models.BooleanField
