import os
from datetime import datetime

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"

def attackToStore():
    n = int(input())
    array = list(map(int, input().split()))
    
    d = [0] * 100
    
    d[0] = array[0]
    d[1] = max(d[0], array[1])
    if d[1] == array[1]:
        print("we attack 1th store")
    else:
        print("we attack 0th store")
        
    for i in range(2, n):
        candidate = d[i-2] + array[i]
        d[i] = max(d[i-1], candidate)
        if d[i] == candidate:
            print(f"we attack {i}th store")
    
    print(d[n-1])

if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")
    
    attackToStore()
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")