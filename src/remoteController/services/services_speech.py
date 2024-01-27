import rospy
from robot_toolkit_msgs.msg import audio_tools_msg, speech_msg
from robot_toolkit_msgs.srv import audio_tools_srv, set_output_volume_srv

def startSpeechMessage():
    #Service speech call
    speechMessage = audio_tools_msg()
    speechMessage.command = "enable_tts"
    speechToolsService(speechMessage)

    #Service audio call
    audioMessage = audio_tools_msg()
    audioMessage.command = "custom"
    audioMessage.frequency = 16000
    audioMessage.channels = 3
    audioToolsService(audioMessage)

def audioToolsService(msg):
    """
    Enables the audio Tools service from the toolkit of the robot.
    """
    print("Waiting for audio tools service")
    rospy.wait_for_service('/robot_toolkit/audio_tools_srv')
    try:
        audio = rospy.ServiceProxy('/robot_toolkit/audio_tools_srv', audio_tools_srv)
        audioService = audio(msg)
        print("Audio tools service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")

def speechToolsService(msg):
    """
    Enables the speech Tools service from the toolkit of the robot.
    """
    print("Waiting for speech tools service")
    rospy.wait_for_service('/robot_toolkit/audio_tools_srv')
    try:
        audio = rospy.ServiceProxy('/robot_toolkit/audio_tools_srv', audio_tools_srv)
        audioService = audio(msg)
        print("Speech tools service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")

def genMsg(language, text):
    """
    Returns a speech_msg for the robot to say.
    """
    t2s_msg = speech_msg()
    t2s_msg.language = language
    t2s_msg.text = text
    t2s_msg.animated = True
    return t2s_msg

def volumeService(volume):
    """
    Changes the volume of the robots output
    """
    print("Waiting for volume tools service")
    rospy.wait_for_service('/pytoolkit/ALAudioDevice/set_output_volume_srv')
    try:
        volumeS = rospy.ServiceProxy('/pytoolkit/ALAudioDevice/set_output_volume_srv', set_output_volume_srv)
        volumeService = volumeS(volume)
        print("Volume service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")