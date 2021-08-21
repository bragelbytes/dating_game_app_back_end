from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    #user path=====
    path('api/useraccount', views.UserList.as_view(), name='user_list'),
    path('api/useraccount/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login"),
    #games path
    path('api/games', views.GamesList.as_view(), name='games_list'),
    path('api/games/<int:pk>', views.GamesDetail.as_view(), name='games_detail')

]
