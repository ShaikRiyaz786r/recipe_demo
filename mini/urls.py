from django.contrib import admin
from django.urls import path,include
from recipes import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/',include(urls))
]
