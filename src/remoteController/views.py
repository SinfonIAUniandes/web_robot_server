# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import shutil
import time

from django.conf import settings
from django.core.files.base import ContentFile
from django.http import StreamingHttpResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from services import services_manipulation as sManipulation
from services import services_miscelanous as sMisc
from services import services_perception as sPerception
from services import services_navigation as sNavigation
from services import services_speech as s_speech


class RemoteC:
    def __init__(self):

        # ROS Publishers
        # self.speechPublisher = rospy.Publisher('/speech',speech_msg,queue_size=10)
        # self.movePublisher = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        # self.headPublisher = rospy.Publisher('/set_angles',set_angles_msg,queue_size=10)
        # self.animationPublisher = rospy.Publisher('/animations',animation_msg,queue_size=10)
        # self.ledsPublisher = rospy.Publisher('/leds',leds_parameters_msg,queue_size=10)

        # ROS Subscribers
        # Suscriber for the robot microphone to get audio
        # self.micSubscriber=rospy.Subscriber("/mic", AudioBuffer, self.audioCallbackSingleChannel)

        # Constants
        self.audioBuffer = ""
        self.ended = False
        self.battery = 100

        # Toolkit messages to turn on robot funcionality
        # sSpeech.startSpeechMessage()
        # sMisc.startMiscMessage()
        # sManipulation.startManipulationMessage()
        # sPerception.startPerceptionMessage()
        # sNavigation.startNavigationMessage()

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


remote = RemoteC()


# Create your views here.
def home(request):
    return render(request, "remoteController/base.html")


def move(request):
    geometry_msg = sNavigation.aux_mov(request.GET["direction"], request.GET["speed"])
    remote.movePublisher.publish(geometry_msg)
    return HttpResponse(status=204)


def joy_stick(request):
    geometry_msg = sNavigation.aux_joy(request.GET["verticalAxis"], request.GET["horizontalAxis"])
    remote.movePublisher.publish(geometry_msg)
    return HttpResponse(status=204)


def speak(request):
    t2s_msg = s_speech.genMsg(request.GET["language"], request.GET["words"])
    remote.speechPublisher.publish(t2s_msg)
    return HttpResponse(status=204)


def display(request):
    sMisc.tabletService(request.GET["url"])
    return HttpResponse(status=204)


def display_web(request):
    sMisc.tabletServiceWeb(request.GET["url"])
    return HttpResponse(status=204)


@csrf_exempt
def save(request):
    imagen = request.FILES['imagen']
    full_filename = os.path.join(settings.MEDIA_ROOT + "/img/", imagen.name.replace(" ", ""))
    fout = open(full_filename, 'wb+')

    file_content = ContentFile(imagen.read())
    for chunk in file_content.chunks():
        fout.write(chunk)
    fout.close()
    sMisc.tabletService("http://192.168.0.250:8000/media/img/" + imagen.name.replace(" ", ""))
    return HttpResponse(status=204)


def animate(request):
    anim_msg = sManipulation.genMsg(request.GET["animation"])
    remote.animationPublisher.publish(anim_msg)
    return HttpResponse(status=204)


def set_leds(request):
    leds_msg = sMisc.genMsg(request.GET["red"], request.GET["green"], request.GET["blue"])
    remote.ledsPublisher.publish(leds_msg)
    time.sleep(0.5)
    return HttpResponse(status=204)


def set_volume(request):
    """
    :param request: HttpRequest object that contains the volume value in the GET parameters.
    :return: HttpResponse with a status code of 204.
    """
    s_speech.volumeService(int(request.GET["volume"]))
    return HttpResponse(status=204)


def get_battery(request):
    """
    Get the battery level.

    :param request: The HTTP request.
    :return: The battery level as an HttpResponse.
    """
    return HttpResponse(str(sMisc.batteryService()))


def get_audio(request):
    """
    Callback for save_audio_srv service: This service allows to record an audio with the microphones of the robot with a duration of x seconds.
    Args:
        seconds (int64): Indicates the duration for recording the audio.
    Returns:
        Returns an answer (string): Indicates if the audio file was created.
    """
    response = StreamingHttpResponse(remote.takeAudioBuffer())
    response['Content-Type'] = 'text/event-stream'
    response['Cache-Control'] = 'no-cache'
    return response


def delete_images(request):
    """
    :delete_images:

    Deletes all images from the media folder.

    :param request: The HTTP request. This parameter is not used in the method.
    :return: An HttpResponse with status code 204 indicating that the images have been successfully deleted.
    """
    folderImagenes = settings.MEDIA_ROOT + "/img/"
    for filename in os.listdir(folderImagenes):
        file_path = os.path.join(folderImagenes, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    return HttpResponse(status=204)


def move_head(request):
    # mover cabeza robot
    jointMsg = sManipulation.genHeadMsg(request.GET["angle0"], request.GET["angle1"])
    remote.headPublisher.publish(jointMsg)
    return HttpResponse(status=204)
