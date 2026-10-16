import os
from datetime import datetime

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"


operatorCnt = 0

def fibo_recursive(n):
    def fibo(x):
        global operatorCnt
        
        if x==1 or x==2:
            return 1
        operatorCnt += 1
        return fibo(x-1) + fibo(x-2)
    print(f"fibo n'th value : {fibo(n)}")
    print(f"called: {operatorCnt}")
        

def fibo_dpBottomUp(n):
    
    dp = [0] * 100
    
    dp[1] = 1
    dp[2] = 1
    
    operatorCnt = 0
    
    for i in range(3, n+1):
        operatorCnt += 1
        dp[i] = dp[i-1] + dp[i-2]
    
    print(f"fibo n'th value : {dp[n]}")
    print(f"called: {operatorCnt}")

def fibo_dpTopdown(n):
    global operatorCnt
    operatorCnt = 0
    
    dp = [0] * 100
    
    def fibo(x):
        global operatorCnt
        
        if x==1 or x==2:
            return 1
        if dp[x] != 0:
            return dp[x]   
        operatorCnt += 1
        
        dp[x] = fibo(x-1) + fibo(x-2)
        return dp[x]
    
    print(f"fibo n'th value : {fibo(n)}")
    print(f"called: {operatorCnt}")

if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")
    
    n = 20
    fibo_recursive(n)
    fibo_dpTopdown(n)
    fibo_dpBottomUp(n)
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")