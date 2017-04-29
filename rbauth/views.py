""" View Render HttpDirect Auth """
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from main.models import UserProfile
from rbauth.validator import Validation
from rbauth.eth_account import EthAccount

# Create an instance of checking methods.
VALID = Validation()
class Signup(View):

    """ Signup View Controller """
    def get(self, request):
        """ Serve signup view """
        title = "サインアップ"
        return render(request, 'pages/signup.html', {'subtitle': title})

    def post(self, request):
        """ Serve signup method """
        # Get POST Data
        # Get inputed data from registering data.
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        student_id = request.POST['id']
        agree = request.POST.getlist('checkbox')

        # Error Status
        error = "None"

        # Registering Data Validation
        # Empty Check
        if VALID.empty([email, username, password]):
            error = "empty"
        # Check overflow
        if VALID.overflow([email, username, password]):
            error = "overflow"
        # Check email and password format
        if VALID.email(email):
            error = "invalidmail"
        if VALID.password(password):
            error = "invalidpass"
        # Check already exists
        if User.objects.filter(username=username).exists():
            error = "ExistsUser"
        if User.objects.filter(email=email).exists():
            error = "ExistsMail"
        # Check license agreement
        if "on" not in agree:
            error = "NotAgree"
        if error == "empty":
            return render(request, 'pages/signup.html', {
                'error': "empty", 'subtitle': "サインアップ"
            })
        elif error == "overflow":
            return render(request, 'pages/signup.html', {
                'error': "overflow", 'subtitle': "サインアップ"
            })
        elif error == "invalidmail":
            return render(request, 'pages/signup.html', {
                'error': "invalidEmail", 'subtitle': "サインアップ"
            })
        elif error == "invalidpass":
            return render(request, 'pages/signup.html', {
                'error': "invalidPass", 'subtitle': "サインアップ"
            })
        elif error == "ExistsUser":
            return render(request, 'pages/signup.html', {
                'error': "doubleUser", 'subtitle': "サインアップ"
            })
        elif error == "ExistsMail":
            return render(request, 'pages/signup.html', {
                'error': "doubleEmail", 'subtitle': "サインアップ"
            })
        elif error == "NotAgree":
            return render(request, 'pages/signup.html', {
                'error': "notAgree", 'subtitle': "サインアップ"
            })
        else:
            # Create user and redirect to login screen.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            eth = EthAccount()
            eth_account = eth.createAccount(password)
            rb_user = UserProfile(
                    user_student_id = student_id,
                    user_ethereum_account = eth_account,
                    user_name_identification = request.user.get_username()
            )
            rb_user.save()

            return HttpResponseRedirect('/login/')
