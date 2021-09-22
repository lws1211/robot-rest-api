# robot-rest-api

1) copy or clone the files into robot-rest-api folder then catkin_make
2) In a terminal, type "rosrun robot-rest-api flk.py", which is the server to subscribe to /move_base/status
3) Wait until the server is ready, in another terminal, type "rosrun robot-rest-api test_flk.py", which poll the REST API poll at 1 Hz rate, then print into the console.

Can launch and move the robot anytime, while REST API will update accordingly.
