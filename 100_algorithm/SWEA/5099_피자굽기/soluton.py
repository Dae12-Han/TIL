from collections import deque

import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    Ci=deque(map(int,input().split()))
    idx=deque(i for i in range(1,M+1))

    #1.deque에 피자를 넣는다.
    #모두 채워지면 그 다음부터 차례가 오는 것들은 한 바퀴를 이미 돈 것들이다!
    oven=deque()
    for _ in range(N):
        oven.append([Ci.popleft(),idx.popleft()]) #치즈, 인덱스

    #2.피자를 구워봅시다~! 
    while oven or Ci:
        pizza=oven.popleft()
        pizza[0]=(pizza[0])//2
        if pizza[0]==0:
            #꺼낼 피자가 남아있다면
            if Ci:
                oven.appendleft([Ci.popleft(),idx.popleft()]) #꺼낸자리에 나머지 피자를 넣는다.
                
        else:
            oven.append(pizza)

        if len(Ci)==0 and len(oven)==1:
            ans=oven[-1][-1]
            break
        
    print(f'#{tc} {ans}')


