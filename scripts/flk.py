#!/usr/bin/env python3

import rospy
import threading
import json
from flask import Flask
from actionlib_msgs.msg import GoalStatusArray
import re



data = GoalStatusArray()



def ros_get_state_callback(goal):  
    global data
    data = goal
    
    
    # rospy.logerr("receiving2")
    
    
threading.Thread(target=lambda: rospy.init_node('server_node', disable_signals=True)).start()
sub = rospy.Subscriber("/move_base/status", GoalStatusArray, ros_get_state_callback)


ip = "127.0.0.1"
port = 7201

app = Flask(__name__)

@app.route("/")
def intro():
    return "hello, please go to http://127.0.0.1:7201/api/robot/status"

@app.route("/api/robot/status")
def get_state():
    topic_list = []
    try:
        topic_list = rospy.get_published_topics(namespace="/move_base/")
    except:
        pass
    
    found = False
    for top in topic_list:
        if "/move_base/status" in top:          
            found = True
    if not found:
        data_set = {"message": "Invalid Status Value"}
        response = app.response_class(
                    response=json.dumps(data_set),
                    status=400)
        rospy.loginfo(response)
        return response
    if len(data.status_list) > 0:
        data_set = {"status":data.status_list[0].status, "text": data.status_list[0].text}
        response = app.response_class(
                    response=json.dumps(data_set),
                    status=200)
        rospy.loginfo(data.status_list[0].text)
        return response
    else:
        data_set = {"status": None, "text": None}
        response = app.response_class(
                    response=json.dumps(data_set),
                    status=200)
        return response


if __name__ == '__main__':
    rospy.loginfo("starting server")
    app.run(host=ip, port=port) 



