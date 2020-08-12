from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from django.http import HttpResponse
import requests
import json
import os

class UserViewSet(viewsets.ModelViewSet):
    '''
    This viewset is attached to the API endpoint.
    '''
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

def show_json(request):
    '''
    Sends a GET request to the API endpoint and parses
    it to an HttpResponse that contains a pretty printed
    JSON containing all the details of users
    '''
    data = requests.get(os.environ.get('HEROKU_APP_NAME') + '/userapi/')
    json_obj = {
        "ok" : True,
        "members" : data.json()
    }
    return HttpResponse(json.dumps(json_obj, indent = 4), content_type = "application/json")