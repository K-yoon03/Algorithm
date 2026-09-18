import os
from datetime import datetime
from collections import deque

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"

def stackExample():
    stack=[]
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    print("before pop stack: ",stack)
    
    popData = stack.pop()
    print("poped data: ", popData)
    print("after pop stack: ", stack)
    
    stack.append(4)
    stack.append(1)
    
    popData = stack.pop()
    print("poped data: ", popData)
    print("after pop stack: ", stack)

    
def queueExample():
    queue= deque()
    '''
    일반 배열에서는 popleft() 사용이 불가능하므로
    deque의 popleft를 사용하여 queue 형태를 의도
    
    dequeue란?
    데크(Dequeue)는 Doubly-ended Queue의 약자로서 양쪽 끝에서 추가, 삭제가 가능한 선형 구조 형태의 자료구조입니다.
    '''
    
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    
    print("before pop queue: ",queue)
    
    popData = queue.popleft()
    print("poped data: ", popData)
    print("after pop queue: ", queue)
    
    queue.append(4)
    queue.append(1)
    print("after appending queue: ",queue)
    
    popData = queue.popleft()
    print("poped data: ", popData)
    print("after pop queue: ", queue)



if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")
    
    # stackExample()
    # queueExample()
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")
