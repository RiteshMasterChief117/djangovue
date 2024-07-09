from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view),
    path('api/posts/', views.api_content_list_view),
    path('api/posts/create/', views.api_content_create_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)