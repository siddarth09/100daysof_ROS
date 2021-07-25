
import rospy 
import actionlib
from learning_ros.msg import washdishesAction,washdishesResult,washdishesFeedback

class washdish():
    def __init__(self):
        self.server=actionlib.SimpleActionServer('washdishes',washdishesAction,self.cb,auto_start=False)
        self.server.start()

    def cb(self,goal):
        
        success=True
        last_dish_washed=''
        
        feedback=washdishesFeedback()
        result=washdishesResult()
        rate=rospy.Rate(1)
        for i in range(0,goal.number_of_minutes):
            if self.server.is_preempt_requested():
                success=False
                break
            last_dish_washed='plate'+str(i)
            feedback.last_dish=last_dish_washed
            result.dishes_washed.append(last_dish_washed)
            self.server.publish_feedback(feedback)
            rate.sleep()
        
        if success:
            self.server.set_succeeded(result)


if __name__=="__main__":
    rospy.init_node('washdish')
    ac=washdish()
    
    


