from django.urls import path, include

urlpatterns = [
    path('', include('user_data.urls')),
]
