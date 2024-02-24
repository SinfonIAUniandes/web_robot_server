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

from services import services_manipulation as sManipulation
from services import miscellaneous_service
from services import services_navigation as sNavigation
from services import services_perception as sPerception
from services import services_speech as sSpeech


class RemoteC:
    def __init__(self):
        # ROS Publishers
        if settings.USE_PEPPER_ROBOT:
            sSpeech.startSpeechMessage()
            miscellaneous_service.startMiscMessage()
            sManipulation.startManipulationMessage()
            sPerception.startPerceptionMessage()
            sNavigation.startNavigationMessage()

            self.speechPublisher = rospy.Publisher('/speech', speech_msg, queue_size=10)
            self.movePublisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
            self.headPublisher = rospy.Publisher('/set_angles', set_angles_msg, queue_size=10)
            self.animationPublisher = rospy.Publisher('/animations', animation_msg, queue_size=10)
            self.ledsPublisher = rospy.Publisher('/leds', leds_parameters_msg, queue_size=10)

            # ROS Subscribers
            # Suscriber for the robot microphone to get audio
            self.micSubscriber = rospy.Subscriber("/mic", AudioBuffer, self.audioCallbackSingleChannel)

        # Constants
        self.audioBuffer = ""
        self.ended = False
        self.battery = 100

    def audioCallbackSingleChannel(self, data):
        """
        Callback for the microphone subcriber of the robot
        """
        audio = data.data
        audio = list(audio)
        for i in audio:
            self.audioBuffer += str(i) + ","
        self.ended = True

    def gen_message(self, msg):
        return '{}'.format(msg)

    def takeAudioBuffer(self):
        while True:
            if self.ended:
                yield self.gen_message(self.audioBuffer)
                self.audioBuffer = ""
                self.ended = False

    def mockAudioBuffer(self):
        f = wave.open(settings.MEDIA_ROOT + "/audio/mario.wav")
        yield f.readframes(1000000)


remote = RemoteC()


# Create your views here.
def home(request):
    return render(request, "remoteController/base.html")


def move(request):
    geometry_msg = sNavigation.aux_mov(request.GET["direction"], request.GET["speed"])
    remote.movePublisher.publish(geometry_msg)
    return HttpResponse(status=204)


def joy_stick(request):
    geometry_msg = sNavigation.aux_joy(request.GET["vertical_axis"], request.GET["horizontal_axis"])
    remote.movePublisher.publish(geometry_msg)
    return HttpResponse(status=204)


def speak(request):
    t2s_msg = sSpeech.genMsg(request.GET["language"], request.GET["text"])
    remote.speechPublisher.publish(t2s_msg)
    return HttpResponse(status=204)


def display(request):
    miscellaneous_service.tabletService(request.GET["url"])
    return HttpResponse(status=204)


def display_web(request):
    miscellaneous_service.tabletServiceWeb(request.GET["url"])
    return HttpResponse(status=204)


@csrf_exempt
def save(request):
    filename = miscellaneous_service.save_image(request.FILES["image"])
    miscellaneous_service.tabletService("http://%s:8000/media/img/%s" % (settings.SERVER_IP, filename))
    return HttpResponse(status=204)


def animate(request):
    anim_msg = sManipulation.genMsg(request.GET["animation"])
    remote.animationPublisher.publish(anim_msg)
    return HttpResponse(status=204)


def set_leds(request):
    leds_msg = miscellaneous_service.genMsg(request.GET["red"], request.GET["green"], request.GET["blue"])
    remote.ledsPublisher.publish(leds_msg)
    time.sleep(0.5)
    return HttpResponse(status=204)

def setVolume(request):
    sSpeech.set_volume_service(int(request.GET["volume"]))
    return HttpResponse(status=204)

def getVolume(request):
    volume = sSpeech.ros_get_volume_service()
    return HttpResponse(volume)

def get_battery(request):
    """
    Get the battery level.

    :param request: The HTTP request.
    :return: The battery level as an HttpResponse.
    """
    return HttpResponse(str(miscellaneous_service.batteryService()))


def get_audio(request):
    """
    Callback for save_audio_srv service: This service allows to record an audio with the microphones of the robot with a duration of x seconds.
    Args:
        seconds (int64): Indicates the duration for recording the audio.
    Returns:
        Returns an answer (string): Indicates if the audio file was created.
    """
    if settings.USE_PEPPER_ROBOT:
        response = StreamingHttpResponse(remote.takeAudioBuffer(), content_type="text/event-stream", status=200)
    else:
        response = StreamingHttpResponse(remote.mockAudioBuffer(), content_type="text/event-stream", status=200)

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
    jointMsg = sManipulation.genHeadMsg(request.GET["angle0"], request.GET["angle1"])
    remote.headPublisher.publish(jointMsg)
    return HttpResponse(status=204)
