from django.conf.global_settings import MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .settings import DEBUG, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("linemetals_api.doc_api")),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_create'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
