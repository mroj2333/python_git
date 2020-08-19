import json

from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse


# Create your views here.

class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass


class ReceiveView(View):
    def get(self, request):
        # 1.接收参数
        data = request.GET
        username = data.get('username')
        password = data.get('password')

        return JsonResponse({'info':{'username':username}})

    def post(self, request):
        data = json.loads(request.body.decode())
        username = data.get('username')
        password = data.get('password')

        return JsonResponse({'info': {'username': username}})
