from trans.models import Transaction
from main.models import UserProfile

class SFCoinTransaction():

    @classmethod
    def getEthAccount(self, username):
        eth_account = UserProfile.objects.get(user_name_identification=username)
        eth = eth_account.user_ethereum_account
        return eth

    @classmethod
    def validateRemaining(self, transfer_amount, username):
        pass
        obj = UserProfile.objects.get(user_name_identification=username)
        remaining = obj.charged_amount

        if remaining < transfer_amount:
            return True

        if remaining == 0:
            return True

        return False



    def Avoid_registerFrom(self, req, username):
        transaction = Transaction(
            from_card = username,
            from_eth_account = self.getEthAccount(username),
        )
        transaction.save()


    def transfer(self, from_u, to_u, amount):
        error = "success"
        if self.validateRemaining(amount, from_u):
            error = "lackOfCharge"
        else:
            from_obj = UserProfile.objects.get(user_name_identification=from_u)
            from_amount = from_obj.charged_amount
            from_amount = int(from_amount) - int(amount)
            UserProfile.objects.filter(user_name_identification=from_u).update(charged_amount=from_amount)

            to = UserProfile.objects.get(user_name_identification=to_u)
            to_amount = to.charged_amount
            to_amount = int(to_amount) + int(amount)
            UserProfile.objects.filter(user_name_identification=to_u).update(charged_amount=to_amount)

        return error
