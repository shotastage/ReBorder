from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.card import CardManager
from trans.trans_manager import SFCoinTransaction
from charge.charge import Charge

class ChargeView(View):
    card = CardManager()
    charge = Charge()

    def get(self, request):
        if request.user.is_authenticated:
            card_user_name = "UNKOWN NAME"
            card_account_number = "PLEASE REGISTER"
            card_remaining_conins = "0 + 0"

            return render(request, 'pages/charge.html',
                {
                    'card_name': card_user_name,
                    'card_account_number': card_account_number,
                    'card_remaining_conins': card_remaining_conins,
                })
        else:
            return render(request, 'pages/login.html')

    def post(self, request):

        req_type = request.POST['post_type']
        charge_target = request.POST['target_user']
        amount = request.POST['amount']

        if req_type == "confirm":

            card_user_name_target = charge_target
            card_account_number_target = self.card.getAccountNumberByUserName(charge_target)
            card_remaining_conins = self.card.getRemainingCoinsByUserName(charge_target)

            return render(request, 'pages/charge.html',
                {
                    'card_name_target': charge_target,
                    'card_account_number_target': card_account_number_target,
                    'amount': amount,
                    'mode': "confirmed",
                    'card_remaining_conins': str(card_remaining_conins) + " + " + str(amount)
                })

        if req_type == "charge":
            self.charge.charge(charge_target, int(amount))
            return HttpResponseRedirect('/diller/')
