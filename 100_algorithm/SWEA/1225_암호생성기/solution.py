import sys
sys.stdin=open('input.txt')

for _ in range(1,11):
    #1.입력
    tc=int(input())
    data_list=list(map(int,input().split()))

    #2.동작 알고리즘
    cycle=0
    while data_list[-1]!=0:
        data=data_list.pop(0)-(cycle%5+1)
        if data<=0: data=0
        data_list.append(data)
        cycle+=1

    #3.출력
    print(f"#{tc}",*data_list)