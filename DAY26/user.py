import rospy
import actionlib
from learning_ros.msg import pizzaGoal,pizzaAction
from rospy import client

def call():
    client=actionlib.SimpleActionClient('dominos_pizza',pizzaAction)
    client.wait_for_server()
    goal=pizzaGoal()
    goal.number_of_pizza=5
    pizza=['margertita','goldencorn','farm house','coke cola','mexican spicy']
    for i in range(5):
        goal.pizza=pizza[i]
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