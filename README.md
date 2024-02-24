
# Web Robot Server

This package allows the hosting of a server that can run in or out of Pepper, this server currently offers a remote controller for the robot and in the future tablet controls.

## Create Workspace

```bash
mkdir interface_ws/src
```
## Installation
To work with the web robot server you need the next packages in your src:

-   robot_toolkit_msgs
-  web_robot_server

To download robot_toolkit_msgs and web_robot_server:
First, browse to your src folder

    cd interface_ws/src
To download robot_toolkit_msgs and web_robot_server:

    git clone https://github.com/SinfonIAUniandes/robot_toolkit_msgs.git
    git clone https://github.com/SinfonIAUniandes/web_robot_server.git

Then go back and build the workspace with catkin_make

    cd ..
    catkin_make

## Environment Variables
The web robot server requires the following environment variables.

    export PEPPER_IP=$(PEPPER_IP)
    export ROS_MASTER_URI=http://$PEPPER_IP:11311
    export ROS_IP=$(ROS_IP)

## Instructions
The manual is available in the docs

## Task list

- [x] Test Django with Ros
- [x] Build a functional backend server
- [x] Install the server in the robot
- [ ] Build the front-end
- [ ] Complete remote controller manual
- [ ] Upgrade the Scripting abilities
- [ ] Add tablet functionality to the server
