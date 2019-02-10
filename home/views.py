from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from .models import *

from .forms import UserForm
gameResponse = "hello, this is the default response"

# Create your views here.


class HomePageView(TemplateView):
    model = User
    gameResponse = 'testtesttesttest'
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = locals()
        context['gameResponse'] = self.gameResponse
        return context

def add_User_Form_Submission(request):
    print("yooooooo")
    _name = request.POST["name"]
    _email = request.POST["email"]
    _kills = 0
    _tokens = 0
    NewUser = User(name = _name, email = _email, kills = _kills, tokens = _tokens)

    NewUser.save()

    return render(request, 'index.html')