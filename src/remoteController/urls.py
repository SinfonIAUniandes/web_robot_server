from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url("api/move", views.move, name="move"),
    url("api/move/head", views.moveHead, name="move_head"),
    url("api/joystick", views.joyStick, name="joyStick"),
    url("api/speak", views.speak, name="speak"),
    url("api/show/image", views.display, name="show_img"),
    url("api/show/web", views.displayWeb, name="show_img_web"),
    url("api/save/image", views.save, name="save_img"),
    url("api/animate", views.animate, name="animate"),
    url("api/set/leds", views.setLeds, name="set_leds"),
    url("api/set/volume", views.setVolume, name="set_volume"),
    url("api/get/battery", views.getBattery, name="get_battery"),
    url("api/get/audio/", views.getAudio, name="getAudio"),
    url("api/delete/images", views.delImgs, name="del_images"),
    url("", views.home, name="home")
]