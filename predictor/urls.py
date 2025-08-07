from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor_form, name='predictor_form'),
    path('predict/', views.predict_emotion, name='predict_emotion'),
]