from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import ObtainAuthToken

from users.views import UserCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', UserCreate.as_view(), name='signup'),
    path('api/login/', ObtainAuthToken.as_view(), name='login'),

    path('', include('images.urls')),
]


# only adding MEDIA ROOT when in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
