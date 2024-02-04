from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url("move/",views.move, name="move"),
    url("joyStick/",views.joyStick, name="joyStick"),
    url("speak/",views.speak, name="speak"),
    url("show_img/",views.display, name="show_img"),
    url("show_web/",views.displayWeb, name="show_img_web"),
    url("save_img/",views.save, name="save_img"),
    url("animate/",views.animate, name="animate"),
    url("setLeds/",views.setLeds, name="setLeds"),
    url("setVolume/",views.setVolume, name="setVolume"),
    url("getVolume/",views.getVolume, name="getVolume"),
    url("getBattery/",views.getBattery, name="getBattery"),
    url("getAudio/",views.getAudio, name="getAudio"),
    url("delImgs/",views.delImgs, name="delImgs"),
    url("moveHead/",views.moveHead, name="moveHead"),
    url("",views.home, name="home")
]