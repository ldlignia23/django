from django.urls import path
from .views import PruebaView
urlpatterns = [
    path('prueba/', PruebaView.as_view(), name="prueba_indexCreate"),
    path('prueba/<int:id>', PruebaView.as_view(), name="prueba_showUpdateDelete"),
]
