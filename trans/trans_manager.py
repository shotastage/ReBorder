from trans.models import Transaction
from main.models import UserProfile

class SFCoinTransaction():

    @classmethod
    def getEthAccount(self, username):
        eth_account = UserProfile.objects.get(user_name_identification=username)
        eth = eth_account.user_ethereum_account
        return eth

    def registerFrom(self, req, username):
        transaction = Transaction(
            from_card = username,
            from_eth_account = self.getEthAccount(username),
        )
        transaction.save()
