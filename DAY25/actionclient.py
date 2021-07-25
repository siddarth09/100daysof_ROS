import rospy
import actionlib
from learning_ros.msg import washdishesAction,washdishesGoal

def feedback_cb(msg):
    print("FEEDBACK:",msg)
def call():
    client= actionlib.SimpleActionClient('washdishes',washdishesAction)
    client.wait_for_server()
    goal=washdishesGoal()
    goal.number_of_minutes=10
    client.send_goal(goal)
    client.wait_for_result()
    result=client.get_result()
    return result

if __name__=="__main__":
    try:
        rospy.init_node('client')
        result=call()
        print("RESULT:",result)
    except rospy.ROSInterruptException:
        print("STOPPED")