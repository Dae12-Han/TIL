import sys
# open을 사용해서 input 파일을 연다
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    #1.입력
    #K=이동할 수 있는 정류장 수,N=종점,M=충전 가능 정류장 수
    K,N,M=map(int,input().split())
    charge_list=list(map(int,input().split()))
    #2.자료형 정의
    #3.동작함수
    bus=N #현재 버스 위치
    cnt=0 #충전소 개수
    can_move=True
    while can_move:
        if bus-K<=0:
            break
        else:
            for idx in range(K,0,-1):
                if bus-idx in charge_list:
                    bus=bus-idx
                    cnt+=1
                    break
                else:
                    if idx==1: #만약 끝까지 돌았는데 없다면
                        can_move=False
                        cnt=0
                        break

    #4.출력
    print(f'#{tc} {cnt}')