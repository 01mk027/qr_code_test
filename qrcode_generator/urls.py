from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_qr_code, name='generate_qr_code'),
    path('redirect-url/', views.redirect_view, name='redirect_url'),  # URL that will be redirected to
]
