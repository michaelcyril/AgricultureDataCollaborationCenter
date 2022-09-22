from django.urls import path
from .views import *


app_name = 'MainInformations'
urlpatterns = [
    path('soil/createPost', PostSoilView),
    path('product/createPost', PostProductView),
    path('home', homeView),
    path('wilayadetails', getWilayaWithInfo),
    path('soil/locations', soilToWilaya),
    path('product/locations', ProductToWilaya),
    path('desease/locations', DeseaseToWilaya),
]