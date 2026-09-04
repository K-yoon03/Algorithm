import time
import random

def maxCalc():
    operand_list = list(map(int, input().split()))
    
    res = 0
    
    for operand in operand_list:
        if operand == 1 or operand == 0:
           res += operand
        else:
            if res == 0 or res == 1:
                res += operand
            else:
                res *= operand
    
    print(f"Max Calculation Result: {res}")

def guild():
    n = int(input())
    fear_list = []
    
    group_cnt = 0
    result = 0
    
    for i in range(0, n):
        fear_list.append(random.randint(1, n))
    
    fear_list.sort()
    
    for fear in fear_list:
        group_cnt += 1
        if group_cnt >= fear:
            result += 1
            group_cnt = 0
    
    print(f"{fear_list}")
    print(f"Groups: {group_cnt} || max_member: {result}")
            

def advancedMakeOne(amount, k):
    res = 0
    while amount != 1:
        print(amount)
        if amount // k != 0:
            target = (amount//k) * k
            res += (amount - target)
            amount -= target
        else:
            amount -= 1
            res += 1
    
    print(f"result: {res}")

def makeone(amount, k):
    cnt_d = 0
    cnt_m = 0
    while amount != 1:
        print(amount)
        if amount % k != 0:
            amount -= 1
            cnt_m += 1
        else:
            amount /= k
            cnt_d += 1 
    
    print(f"Division: {cnt_d} || Minus: {cnt_m}")

def greedy(amount):
    bill_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = 0
    for bill in bill_list:
        cnt += amount // bill
        amount %= bill
        print(f"{bill}won : {cnt}")
        cnt = 0

if __name__ == "__main__":
    maxCalc()
    #guild()
    #advancedMakeOne(25, 3)
    #makeone(25, 3)
    #greedy(958630)