document.addEventListener('DOMContentLoaded', function ()
{
    var front_camera = document.getElementById("front_camera");
    front_camera.src = "http://"+ip+":8080/stream?topic=/robot_toolkit_node/camera/front/image_raw";
    var bottom_camera = document.getElementById("bottom_camera");
    bottom_camera.src = "http://"+ip+":8080/stream?topic=/robot_toolkit_node/camera/bottom/image_raw";
})