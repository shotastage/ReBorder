from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import UserProfile


class MainView(View):
    def get(self, request):
        if request.user.is_authenticated:
            #if UserProfile.objects
            return render(request, 'pages/index.html')
        else:
            return render(request, 'pages/login.html')
