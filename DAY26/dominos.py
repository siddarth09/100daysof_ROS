import rospy
import actionlib
from learning_ros.msg import pizzaAction,pizzaFeedback,pizzaResult

class dominos():
    def __init__(self) -> None:
        self.server=actionlib.SimpleActionServer('dominos_pizza',pizzaAction,self.cb,auto_start=False)
        self.server.start()

    def cb(self,goal):
        success=True
        last_pizza=''
        feedback=pizzaFeedback()
        result=pizzaResult()
        rate=rospy.Rate(1)
        for i in range(0,goal.number_of_pizza):
            if self.server.is_preempt_requested():
                success=False
                break
            last_pizza=goal.pizza
            feedback.last_pizza=last_pizza
            result.pizzas.append(last_pizza)
            self.server.publish_feedback(feedback)
            rate.sleep()
        if success:
            self.server.set_succeeded(result)

if __name__=="__main__":
    rospy.init_node('dominos')
    ac=dominos()