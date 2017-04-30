from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.card import CardManager
from trans.trans_manager import SFCoinTransaction


class Transfer(View):
    card = CardManager()
    coin = SFCoinTransaction()

    def get(self, request):
        if request.user.is_authenticated:
            card_user_name = self.card.getUserFullName(request)
            card_account_number = self.card.getAccountNumber(request)
            card_remaining_conins = self.card.getRemainingCoins(request)

            return render(request, 'pages/transfer.html',
                {
                    'card_name': card_user_name,
                    'card_account_number': card_account_number,
                    'card_remaining_conins': card_remaining_conins,
                })
        else:
            return render(request, 'pages/login.html')

    def post(self, request):
        req_type = request.POST['post_type']

        if req_type == "transfer":
            return HttpResponseRedirect('/diller/')
        if req_type == "confirm":
            #self.coin.registerFrom(request, request.user.get_full_name())
            from_user = request.POST['from_user']
            to_user = request.POST['to_user']
            amount = request.POST['amount']


            card_user_name_from = from_user
            card_account_number_from = self.card.getAccountNumberByUserName(from_user)

            card_user_name_to = to_user
            card_account_number_to = self.card.getAccountNumberByUserName(to_user)

            return render(request, 'pages/transfer.html',
                {
                    'card_name_from': card_user_name_from,
                    'card_account_number_from': card_account_number_from,
                    'card_name_to': card_user_name_to,
                    'card_account_number_to': card_account_number_to,
                    'amount': amount,
                    'mode': "confirmed"
                })
