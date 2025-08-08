import sys
sys.stdin=open('input.txt')

from collections import deque

def park(x):
    for i in range(1,n+1):
        if parking[i]==False:
            parking[i]=True
            return i
    else:
        return 0

T=int(input())
for tc in range(1,T+1):
    ans=0

    n,m=map(int,input().split())
    costs=deque([0]) #단위 무게당 요금
    for _ in range(n):
        costs.append(int(input()))
    cars=deque([0])     #차량의 무게
    for _ in range(m):
        cars.append(int(input()))

    parking=[False for _ in range(n+1)] #주차 여부
    pos=[0 for _ in range(m+1)]         #자동차가 주차한 곳
    queuing=deque() #대기줄
    for _ in range(m*2):
        x=int(input())
        if x>0:
            xi=park(x)
            if xi==0:
                queuing.append(x)
                continue
            else:
                pos[x]=xi
                ans+=(cars[x]*costs[pos[x]])
        else:
            x=abs(x)
            parking[pos[x]]=False
            if queuing:
                nx=queuing.popleft()
                pos[nx]=park(nx)
                ans+=(cars[nx] * costs[pos[nx]])

    print(f'#{tc} {ans}')
