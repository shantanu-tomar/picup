from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from users.views import UserCreate, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('images.urls')),
    path('api/signup/', UserCreate.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    re_path('^.*$', TemplateView.as_view(template_name="index.html"), name="wildcard"),
]


# only adding MEDIA ROOT when in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
