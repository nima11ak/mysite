from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),  # 👈 مسیر اپ website
    path('Blog/',include('Blog.urls'))
]



urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)