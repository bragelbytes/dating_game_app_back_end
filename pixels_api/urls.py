from django.urls import path
from . import views

urlpatterns = [
    #user path=====
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    #games path
    path('api/games', views.GamesList.as_view(), name='games_list'),
    path('api/games/<int:pk>', views.GamesDetail.as_view(), name='games_detail')

]
