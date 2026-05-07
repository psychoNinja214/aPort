from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projects.views import project_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project_list, name='home'),
    path('projects/', include('projects.urls')),
    path('contact/', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
