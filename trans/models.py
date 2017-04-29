from django.db import models

# Create your models here.

class Transaction(models.Model):

    # From
    from_card = models.CharField(max_length=100)
    from_eth_account = models.CharField(max_length=100)

    # To
    to_card = models.CharField(max_length=100)
    to_eth_account = models.CharField(max_length=100)

    # Transfer Coins
    amount = models.IntegerField