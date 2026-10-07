import os
from datetime import datetime

def getCurrentTimerStr():
    currentTimerStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"[:-3])
    return "["+currentTimerStr+"]"


def binarySearchExam():
    n, target = map(int, input("Input data amount of N and target data: (N target)").split())
    array = list(map(int, input(f"Input actual data amount of {n}:").split()))
    
    targetIdx = binarySearch(array, target, 0, n-1)

    if targetIdx == None:
        print(f"There isn't target data. ({target})")
    else:
        print(f"Finding data({target}) is array[{targetIdx}]")
    
## 주어진 array의 start 위치~ end 위치까지 중, target을 찾고
## 찾은 경우 위치를 반환, 없으면 None을 반환
def binarySearch(array, target, start, end):
    ## 마지막까지 1개도 없다면 target이 없는 것으로 종료
    if end < start:
        return None
    
    ## 중간 위치를 결정
    # mid = int((start + end) / 2)
    mid = (start + end) // 2
    # 둘의 실행 결과는 동일.
    
    ## 중간 위치의 데이터와 target을 비교
    ## 같다면, 그 중간위치가 target의 위치
    if array[mid] == target:
        return mid
    ## target이 더 크면 중간위치 다음부터 end까지 재귀 호출
    elif target > array[mid]:
        binarySearch(array, target, mid+1, end)
    ## target이 더 작은 경우, start부터 (중간-1)까지 재귀호출
    # elif target < array[mid]:
    else:
        binarySearch(array, target, start, mid-1)
    # 코드의 완결성을 위해 array와 mid가 숫자타입인 경우 같거나 크거나 작은 경우밖에 없으므로 else로 마무리


if __name__ == "__main__":
    startTime = datetime.now()
    print(getCurrentTimerStr(), "Main function is Start")

    binarySearchExam()
    
    finishTime = datetime.now()
    print(getCurrentTimerStr(), f"{(finishTime-startTime).total_seconds()}s is elapsed")
