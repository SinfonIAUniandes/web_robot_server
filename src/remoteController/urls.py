from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url("api/move", views.move, name="move"),
    url("api/move/head", views.move_head, name="move_head"),
    url("api/joystick", views.joy_stick, name="joyStick"),
    url("api/speak", views.speak, name="speak"),
    url("api/show/image", views.display, name="show_img"),
    url("api/show/web", views.display_web, name="show_img_web"),
    url("api/save/image", views.save, name="save_img"),
    url("api/animate", views.animate, name="animate"),
    url("api/set/leds", views.set_leds, name="set_leds"),
    url("api/set/volume", views.set_volume, name="set_volume"),
    url("api/get/battery", views.get_battery, name="get_battery"),
    url("api/get/audio", views.get_audio, name="getAudio"),
    url("api/delete/images", views.delete_images, name="delete_images"),
    url("", views.home, name="home")
]