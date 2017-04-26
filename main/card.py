from django.contrib.auth.models import User


class CardManager():

    def getUserFullName(self, req):
        full_name = req.user.get_full_name().upper()
        return full_name

    def getAccountNumber(self):
        return "0000-0000-0000-00"

    def getRemainingCoins(self):
        return "0000"
