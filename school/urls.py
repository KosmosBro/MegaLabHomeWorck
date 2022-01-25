from django.urls import path
import school.views as v

urlpatterns = [
    path('', v.view_login, name='home'),
    path('register', v.view_register, name='register')
]
