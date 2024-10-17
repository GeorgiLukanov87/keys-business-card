from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kluchar_mister_minut_varna.web_page.urls'))
]
