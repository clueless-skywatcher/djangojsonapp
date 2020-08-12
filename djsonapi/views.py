from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User, ActivityPeriod
from django.http import JsonResponse, HttpRequest, HttpResponse
import requests
import json
import os

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

def show_json(request):
    data = requests.get(os.environ.get('HEROKU_APP_NAME') + '/userapi/')
    json_obj = {
        "ok" : True,
        "members" : data.json()
    }
    return HttpResponse(json.dumps(json_obj, indent = 4), content_type = "application/json")