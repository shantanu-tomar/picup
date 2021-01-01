from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import UserCreate, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('images.urls')),
    path('api/signup/', UserCreate.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
]


# only adding MEDIA ROOT when in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
