from django.urls import path
from . import views  # This is where views are being correctly imported from

urlpatterns = [
    path('webhook/', views.webhook_receiver, name='webhook_receiver'),
    path('ping/',views.PingView.as_view())
]
