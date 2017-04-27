from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import UserProfile

# Import modules
from main.card import CardManager
from main.game_session import GameSession

class MainView(View):

    card = CardManager()

    def get(self, request):
        if request.user.is_authenticated:
            card_user_name = self.card.getUserFullName(request)
            card_account_number = self.card.getAccountNumber()
            card_remaining_conins = self.card.getRemainingCoins()

            return render(request, 'pages/index.html',
                {
                    'card_name': card_user_name,
                    'card_account_number': card_account_number,
                    'card_remaining_conins': card_remaining_conins,
                })
        else:
            return render(request, 'pages/login.html')


class DillerView(View):

    card = CardManager()

    def get(self, request):
        if request.user.is_authenticated:
            card_user_name = self.card.getUserFullName(request)
            card_account_number = self.card.getAccountNumber()
            card_remaining_conins = self.card.getRemainingCoins()

            return render(request, 'pages/diller.html',
                {
                    'card_name': card_user_name,
                    'card_account_number': card_account_number,
                    'card_remaining_conins': card_remaining_conins,
                })
        else:
            return render(request, 'pages/login.html')


class DillerSessionView(View):
    sess = GameSession()

    session_info = ("", "")

    def get(self, request):
        if request.user.is_authenticated:
            self.session_info = self.sess.createSession()
            self.sessino_id = self.session_info[1]
            return render(request, 'pages/session.html', {
                'session_pin': self.session_info[1]
            })
        else:
            return render(request, 'pages/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            req_type = request.POST['post_type']
            if req_type == "end_session":
                self.sess.revokeSession(self.session_info)
                return HttpResponseRedirect('/')
        else:
            return render(request, 'pages/login.html')
