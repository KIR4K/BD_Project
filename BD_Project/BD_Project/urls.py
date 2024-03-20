from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls,name= 'admin'),
    path('',admin.site.urls),
    path('get_loan/',include('client.urls'))
]
