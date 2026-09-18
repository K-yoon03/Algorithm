import os
from datetime import datetime

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"

def dfs_icing(graph, n, m, x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs_icing(graph, n, m, x -1, y)
        dfs_icing(graph, n, m, x, y-1)
        dfs_icing(graph, n, m, x + 1, y)
        dfs_icing(graph, n, m, x, y + 1)
        return True
    return False

def freezeIcecream(n, m):
    graph = []
    
    for i in range(n):
        graph.append(list(map(int, input())))
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs_icing(graph, n, m, i, j) == True:
                result += 1
    
    return result

if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")
    
    n, m = map(int,input().split())
    
    iceframe = freezeIcecream(n, m)
    
    print("How many icecream? \nanswer: ", iceframe)
    
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")
