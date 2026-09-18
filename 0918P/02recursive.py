import os
from datetime import datetime

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"

def recursive_prep(stack):
    
    if stack:
        popData = stack.pop()
        print ("pop this!", popData)
        recursive_prep(stack)
        
    else:
        print("Stack is empty")
    
def factorial_iterative(n):
    if n <= 1:
        return 1
    return n * factorial_iterative(n-1)

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    '''
    a % b가 R
    '''



    
if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")
    
    
    # stack = [1,7,2,6,62,7,15,74,4,32,81,7,8,65,4,1,1]
    # recursive_prep(stack)
    
    # print(factorial_iterative(4))
    
    print(gcd(192,162))
    
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")
