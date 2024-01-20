# yourapp/views.py

import requests, json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

import os


# from rest_framework import permissions

class AccessTokenView(View):
    # permison_classes = (permissions.AllowAny, )
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        # 1. GET 매개변수에서 코드를 추출합니다.
        code = request.GET.get('code', None)

        if not code:
            return HttpResponse("요청에서 코드가 제공되지 않았습니다.", status=400)

        # 2. 추출한 코드를 사용하여 access token을 요청합니다.
        base_url = "https://api.intra.42.fr/oauth/token"
        client_id = os.environ.get("UID")
        client_secret = os.environ.get("SECRET")
        redirect_uri = os.environ.get("REDIRECT_URI")
        scope = "public"

        data = {
            'grant_type': "authorization_code",
            'code': code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
            'scope': scope,
        }

        headers = {
            'Content-Type': 'application/json'
        }

        print("Data sent to OAuth server:", data)
        response = requests.post(base_url, data=json.dumps(data), headers=headers)
        print ("Response is : ", response.json())
        
        if response.status_code == 200:
            # 성공적인 응답이면 access token을 사용할 수 있습니다.
            access_token = response.json().get('access_token')
            user_response = requests.get("https://api.intra.42.fr/v2/me", headers={"Authorization": f"Bearer {access_token}"})
            
            username = user_response.json()["login"]
            # email = user_response.json()["email"]
            # picture_url = user_response.json()["image"]["versions"]["medium"]
            
            from django.contrib.auth.models import User
            user = User.objects.get_or_create(username=username)

            return HttpResponse(f"Access Token: {access_token}\nUsername: {username}\n")
        else:
            # 오류를 적게 처리합니다.
            return HttpResponse(f"Access token을 가져오는 중 오류 발생. 상태 코드: {response.status_code}", status=response.status_code)
        
