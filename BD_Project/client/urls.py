from django.urls import path
from . import views

urlpatterns = [
    path('form_1/',views.form_1,name = 'form_1'),
    path('form_2/<int:client_id>/',views.form_2,name = 'form_2'),
]
