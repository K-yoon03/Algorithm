'''
    문제: 두 개의 배열 A와 B가 제공된다.
        두 배열의 요소를 K번 바꿀 수 있으며, K번 바꿨을 때
        배열 A의 합이 가장 높게 될 수 있게 변경한다.
        N은 1000000 이하로 주어진다.
'''
import sys

# N과 K를 입력받는다.
N, K = map(int, input("Input N, K:").split())

# N이 100만이 넘어갈 경우 프로그램을 종료한다.
if N > 1000000:
    sys.exit(0)

# 각 A B 배열을 입력받는다.
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

# A와 B를 정렬한다. 단 B의 경우 역순정렬하여 높은값을 앞으로 오게 한다.
# A와 B가 정렬이 반대로 되었을 경우 각 index만 비교하면 되기 때문.
arrayA.sort()
arrayB.sort(reverse=True)

for i in range(K):
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else:
        break

print(sum(arrayA))


