import os
from datetime import datetime

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"

def tteokbugiSlayer():
    n, m = map(int, input("How many do you have tteok? and how long does customer want?: ").split())
    array = list(map(int, input("How long is tteok?").split()))
    
    res = tteokbugi(array, m)
    print(f"We served tteok {res}cm")

def tteokbugi(array, m):
    start, end = 0, max(array)
    res = 0
    
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        
        for x in array:
            if x > mid:
                total += x - mid
        if total < m:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    print(f"We sliced at {res}cm")
    return total

if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")
    
    tteokbugiSlayer()
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")