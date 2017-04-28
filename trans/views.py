from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.card import CardManager


class Transfer(View):
    card = CardManager()

    def get(self, request):
        if request.user.is_authenticated:
            card_user_name = self.card.getUserFullName(request)
            card_account_number = self.card.getAccountNumber()
            card_remaining_conins = self.card.getRemainingCoins()

            return render(request, 'pages/transfer.html',
                {
                    'card_name': card_user_name,
                    'card_account_number': card_account_number,
                    'card_remaining_conins': card_remaining_conins,
                })
        else:
            return render(request, 'pages/login.html')
