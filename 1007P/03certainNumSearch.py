import os
from datetime import datetime
from bisect import bisect_left, bisect_right

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"

def solution():
    n, target = map(int, input("Input size of list N, target M ").split())
    array = list(map(int, input("Input element of list ").split()))
    
    minIdx = bisect_left(array, target)
    maxIdx = bisect_right(array, target)
    
    count = maxIdx - minIdx
    
    if count == 0:
        return -1
    else:
        return count

if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")
    
    print(f"{solution()}")
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")