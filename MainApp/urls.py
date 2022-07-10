from django.contrib import admin
from django.urls import path,include
from .import views
#For lower section if in DEBUG mode
from FunJoystick import settings
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('contact',views.contact,name="contact"),
    path('response',views.response,name="response"),
    path('home',views.home,name="home"),
    path('playgames',views.playgames,name="playgames"),
    path('searchGames',views.searchGames,name="searchGames"),
    path('searchDownloads',views.searchDownloads,name="searchDownloads"),
    path('snakegame',views.snake,name="snakegame"),
    path('startfall',views.startFall,name="startfall"),
    path('fallball',views.fallBall,name="fallball"),
    path('tictactoe',views.ticTacToe,name="tictactoe"),
    path('CPU',views.CPU,name="CPU"),
    path('flappybird',views.flappyBird,name="flappybird"),
    path('robot',views.robot,name="robot"),
    path('robot2',views.robot2,name="robot2"),
    path('downloads',views.downloads,name="downloads"),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

if (settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)