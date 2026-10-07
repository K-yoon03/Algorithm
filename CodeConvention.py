import os
from datetime import datetime

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"


if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")
    
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")