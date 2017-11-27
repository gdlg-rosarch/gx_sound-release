#! /usr/bin/env python
# -*- coding: utf-8 -*-

import actionlib
import os
import rospy

from gx_sound_msgs.msg import SoundRequestAction, SoundRequestGoal


def main():
    rospy.init_node('sound_request_client_node')
    client = actionlib.SimpleActionClient('/gx_sound_player/sound_player/sound_request', SoundRequestAction)
    client.wait_for_server()
    rospy.loginfo("connected to actionlib server")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    now = rospy.get_rostime()

    # 逆順に送信しても時刻順に再生される
    goal1 = SoundRequestGoal(stamp=rospy.Time(secs=now.to_sec() + 3.0), file=os.path.join(base_dir, "audio3.wav"))
    goal2 = SoundRequestGoal(stamp=rospy.Time(secs=now.to_sec() + 2.0), file=os.path.join(base_dir, "audio2.wav"))
    goal3 = SoundRequestGoal(stamp=rospy.Time(secs=now.to_sec() + 1.0), file=os.path.join(base_dir, "audio1.wav"))

    # Fill in the goal here
    rospy.loginfo("send request")
    client.send_goal(goal1)
    client.send_goal(goal2)
    client.send_goal(goal3)
    rospy.loginfo("waiting for result")
    client.wait_for_result(rospy.Duration.from_sec(5.0))


if __name__ == '__main__':
    main()
