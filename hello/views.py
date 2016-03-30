import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

#Add to header of your file
from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.objects import AdUser


# Create your views here.
def index(request):
    #Initialize a new Session and instanciate an Api object
    my_app_id = '1672585882991034'
    my_app_secret = '38c9b5fba3cf14297b1da57832c45057'
    my_access_token = 'CAAXxNT9peboBAG7SNVFXKOm8NillZAQxQLWXIf2N1PZArEpKZCpMTYZCZAGLZBYq0Gdzq7E1l90I7GlIBN2lLpON37JZBzwuADu7iJk7QByBYyeHAsUr62TTiS9wOBkd9JezaZCZCZB6MnSizo5VftYYVnt5rjQ1gDmTgALKIoPxPZC560jJij88hsvXFu64xaiDjnWTFWqSZAiIPwZDZD' 
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    #Add after FacebookAdsApi.init
    me = AdUser(fbid='me')
    my_account = me.get_ad_accounts()[0]
    print my_account

    return HttpResponse('Hello from Python!')

    # return HttpResponse('Hello from Python!')
    # r = requests.get('http://httpbin.org/status/418')
    # print r.text
    # return HttpResponse('<pre>' + r.text + '</pre>')

    
    

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

