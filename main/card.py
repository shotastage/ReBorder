from django.contrib.auth.models import User
from main.models import UserProfile

class CardManager():

    @classmethod
    def split_str(self, str, length):
        v = [str[i: i+length] for i in range(0, len(str), length)]
        return v

    @classmethod
    def cryptAccountNumber(self, num):
        tmp = self.split_str(num, 3)
        account_number = ""
        for num in tmp:
            tmp2 = self.split_str(num, 1)

            if len(num) == 1:
                determined_num = num[0]
                break

            determined_num = int(tmp2[0]) * int(tmp2[1]) * int(tmp2[2])
            account_number = account_number + str(determined_num)

        return account_number

    @classmethod
    def determineAccountNumber(self, num):
        tmp = self.cryptAccountNumber(self.cryptAccountNumber(num))
        tmp2 = self.split_str(tmp, 2)

        num = ""

        for n in tmp2:
            a = int(n[0]) + int(n[0])

            num = num +str(a)

        return num

    def getUserFullName(self, req):
        obj = UserProfile.objects.get(user_name_identification=req.user.get_username())
        full_name = req.user.get_full_name().upper()
        return full_name

    def getUserFullNameByUserName(self, username):

        name_obj = User.objects.get(username=username)
        f_name = name_obj.first_name
        l_name = name_obj.last_name

        full_name = f_name + " " + l_name
        full_name = full_name.upper()
        return full_name

    def getAccountNumber(self, req):
        obj = UserProfile.objects.get(user_name_identification=req.user.get_username())

        # Convert string to 16
        eth_account = "0x" + obj.user_ethereum_account
        integer_account_no = str(int(eth_account, 16))

        account_number = self.determineAccountNumber(integer_account_no)

        return account_number

    def getAccountNumberByUserName(self, username):
        obj = UserProfile.objects.get(user_name_identification=username)

        # Convert string to 16
        eth_account = "0x" + obj.user_ethereum_account
        integer_account_no = str(int(eth_account, 16))

        account_number = self.determineAccountNumber(integer_account_no)

        return account_number

    def getRemainingCoins(self, req):
        amount_obj = UserProfile.objects.get(user_name_identification=req.user.get_username())
        amount = amount_obj.charged_amount
        return str(amount)
