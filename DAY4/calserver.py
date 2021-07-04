from learning_ros.srv import calculator
from learning_ros.srv import calculatorRequest
from learning_ros.srv import calculatorResponse
import rospy

def basic_calculator (nb1, nb2, op):
    result = 0 # write your code to perform the operation & return the good result
    
    if  op =='+':
        result=nb1+nb2
        
    elif op=='-':
        result=nb1-nb2
       
    elif op=='*':
        result=nb1*nb2
        
    elif op=='/':
        try:
            result=nb1/nb2
            
        except ZeroDivisionError:
            result="Can’t divide by 0"
    
    return result

def callback_calci(req):
    result = 0 # write your code to perform the operation & return the good result
    
    if  str(req.symbol)=='+':
        result=req.a+req.b
        
    elif str(req.symbol)=='-':
        result=req.a-req.b
       
    elif str(req.symbol)=='*':
        result=req.a*req.b
        
    elif str(req.symbol)=='/':
        
        try:
            result=req.a/req.b
            
        except ZeroDivisionError:
            result="Can’t divide by 0"
    
    return calculatorResponse(result)
    
def calculate():
    rospy.init_node('Calculator')
    s= rospy.Service('calci',calculator,callback_calci)
    print("calculator starting ")
    rospy.spin()

if __name__=="__main__":
    calculate()