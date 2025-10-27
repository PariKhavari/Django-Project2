from django.urls import path
from .views import info_fruits, send_fruits

app_name = 'fruit_app2'

urlpatterns = [
    path('', send_fruits),
    path('info/', info_fruits),

]
