from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login_views, name='login'),
    path('logout/', logout_views, name='logout'),
    path('signup/', signup_views, name='signup')
]
