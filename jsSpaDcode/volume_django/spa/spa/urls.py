# # """spa URL Configuration

# # The `urlpatterns` list routes URLs to views. For more information please see:
# #     https://docs.djangoproject.com/en/1.10/topics/http/urls/
# # Examples:
# # Function views
# #     1. Add an import:  from my_app import views
# #     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# # Class-based views
# #     1. Add an import:  from other_app.views import Home
# #     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# # Including another URLconf
# #     1. Import the include() function: from django.conf.urls import url, include
# #     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# # """
# # from django.conf.urls import url
# # from django.contrib import admin

# # urlpatterns = [
# #     url(r'^admin/', admin.site.urls),
# # ]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.views.static import serve
# from django.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# static 파일들에 대한 처리입니다.
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 모든 요청에 대해 index.html을 서빙합니다.
urlpatterns += [url(r'^.*$', serve, kwargs={'path': 'index.html'})]
