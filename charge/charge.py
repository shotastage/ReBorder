from main.models import UserProfile


class Charge:

    def charge(self, username, amount):
        current_amount = UserProfile.objects.get(user_name_identification=username)
        update_amount = current_amount.charged_amount + amount
        UserProfile.objects.filter(user_name_identification=username).update(charged_amount=update_amount)
