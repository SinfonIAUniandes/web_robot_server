# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import wave

import rospy
from django.conf import settings
from django.http import StreamingHttpResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from geometry_msgs.msg import Twist
from naoqi_bridge_msgs.msg import AudioBuffer
from robot_toolkit_msgs.msg import speech_msg, set_angles_msg, animation_msg, leds_parameters_msg

from services import manipulation_services
from services import miscellaneous_service
from services import navigation_services
from services import perception_services
from services import speech_services


class RemoteC:
    def __init__(self):
        # ROS Publishers
        if settings.USE_PEPPER_ROBOT:
            speech_services.start_speech_message()
            miscellaneous_service.start_misc_message()
            manipulation_services.start_manipulation_message()
            perception_services.start_perception_message()
            navigation_services.start_navigation_message()

            self.speech_publisher = rospy.Publisher('/speech', speech_msg, queue_size=10)
            self.move_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
            self.head_publisher = rospy.Publisher('/set_angles', set_angles_msg, queue_size=10)
            self.animation_publisher = rospy.Publisher('/animations', animation_msg, queue_size=10)
            self.leds_publisher = rospy.Publisher('/leds', leds_parameters_msg, queue_size=10)

            # ROS Subscribers
            # Suscriber for the robot microphone to get audio
            self.mic_subscriber = rospy.Subscriber("/mic", AudioBuffer, self.audio_callback_single_channel)

        # Constants
        self.audio_buffer = ""
        self.ended = False
        self.battery = 100

    def audio_callback_single_channel(self, data):
        """
        Callback for the microphone subcriber of the robot
        """
        audio = data.data
        audio = list(audio)
        for i in audio:
            self.audio_buffer += str(i) + ","
        self.ended = True

    def generate_message(self, msg):
        return '{}'.format(msg)

    def take_audio_buffer(self):
        while True:
            if self.ended:
                yield self.generate_message(self.audio_buffer)
                self.audio_buffer = ""
                self.ended = False


    def mock_audio_buffer(self):
        f = wave.open(settings.MEDIA_ROOT + "/audio/mario.wav")
        yield f.readframes(1000000)


remote = RemoteC()


# Create your views here.
def home(request):
    return render(request, "remoteController/base.html")


def move(request):
    geometry_msg = navigation_services.aux_mov(request.GET["direction"], request.GET["speed"])
    if settings.USE_PEPPER_ROBOT:
        remote.move_publisher.publish(geometry_msg)
    return HttpResponse(status=204)


def joy_stick(request):
    geometry_msg = navigation_services.aux_joy(request.GET["vertical_axis"], request.GET["horizontal_axis"])
    if settings.USE_PEPPER_ROBOT:
        remote.move_publisher.publish(geometry_msg)
    return HttpResponse(status=204)


def speak(request):
    t2s_msg = speech_services.generate_message(request.GET["language"], request.GET["text"])
    if settings.USE_PEPPER_ROBOT:
        remote.speech_publisher.publish(t2s_msg)
    return HttpResponse(status=204)


def show_image(request):
    miscellaneous_service.show_img_service(request.GET["url"])
    return HttpResponse(status=204)


def show_web(request):
    miscellaneous_service.show_web_service(request.GET["url"])
    return HttpResponse(status=204)


@csrf_exempt
def save_image(request):
    filename = miscellaneous_service.save_image(request.FILES["image"])
    miscellaneous_service.show_img_service("http://%s:8000/media/img/%s" % (settings.SERVER_IP, filename))
    return HttpResponse(status=204)


def animate(request):
    anim_msg = manipulation_services.generate_message(request.GET["animation"])
    if settings.USE_PEPPER_ROBOT:
        remote.animation_publisher.publish(anim_msg)
    return HttpResponse(status=204)


def set_leds(request):
    leds_msg = miscellaneous_service.generate_message(request.GET["red"], request.GET["green"], request.GET["blue"])
    if settings.USE_PEPPER_ROBOT:
        remote.leds_publisher.publish(leds_msg)
    time.sleep(0.5)
    return HttpResponse(status=204)


def set_volume(request):
    speech_services.set_volume_service(int(request.GET["volume"]))
    return HttpResponse(status=204)


def get_volume(request):
    volume = speech_services.ros_get_volume_service()
    return HttpResponse(volume)


def get_battery(request):
    """
    Get the battery level.

    :param request: The HTTP request.
    :return: The battery level as an HttpResponse.
    """
    return HttpResponse(str(miscellaneous_service.battery_service()))


def get_audio(request):
    """
    Callback for save_audio_srv service: This service allows to record an audio with the microphones of the robot with a duration of x seconds.
    Args:
        seconds (int64): Indicates the duration for recording the audio.
    Returns:
        Returns an answer (string): Indicates if the audio file was created.
    """
    if settings.USE_PEPPER_ROBOT:
        response = StreamingHttpResponse(remote.take_audio_buffer(), content_type="text/event-stream", status=200)
    else:
        response = StreamingHttpResponse(remote.mock_audio_buffer(), content_type="text/event-stream", status=200)

    response["Cache-Control"] = "no-cache"
    return response


def delete_images():
    """
    :delete_images:

    Deletes all images from the media folder.
    """
    miscellaneous_service.remove_images()
    return HttpResponse(status=204)


def move_head(request):
    # mover cabeza robot
    joint_msg = manipulation_services.generate_head_message(request.GET["angle0"], request.GET["angle1"])
    if settings.USE_PEPPER_ROBOT:
        remote.head_publisher.publish(joint_msg)
    return HttpResponse(status=204)
