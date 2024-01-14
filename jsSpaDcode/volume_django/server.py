from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    # 다른 url 패턴들...
]

# static 파일들에 대한 처리입니다.
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 모든 요청에 대해 index.html을 서빙합니다.
urlpatterns += [re_path(r'^.*$', serve, kwargs={'path': 'index.html'})]
