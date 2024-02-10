#!/usr/bin/env python
import os
import sys
import rospy

if __name__ == "__main__":
    rospy.init_node("web_robot_server")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webRobotServer.settings")
    print("="*10 + " WEB ROBOT SERVER " + "="*10)
    print("- Node successfully initialized")
    print("="*18 + "="*10)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
