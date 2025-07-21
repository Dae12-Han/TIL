T=int(input())
for t in range(T):
    #1.입력
    N,M=map(int,input().split())
    matrix=[list(map(int,input().split())) for _ in range(N)]
    #2.자료형 정의
    #3.동작함수
    max_fly=0

    # + 형태
    for y in range(N):
        for x in range(N):
            fly1=0
            for m in range(-M+1,M): 
                nx=x+m
                ny=y+m
                if m==0:
                    fly1+=matrix[ny][nx]
                else:
                    if 0<=nx<N:
                        fly1+=matrix[y][nx]
                    if 0<=ny<N:
                        fly1+=matrix[ny][x]
            max_fly=max(fly1,max_fly)

    # x 형태
    for y in range(N):
        for x in range(N):
            fly2=0
            fly2+=matrix[y][x]
            for m1 in range(-M+1,M):
                nx=x+m1
                if m1==0: 
                    continue
                if 0<=nx<N:
                    for m2 in range(-M+1,M):
                        ny=y+m2
                        if m2==0:
                            continue
                        if 0<=ny<N:
                            fly2+=matrix[ny][nx]
            max_fly=max(fly2,max_fly)
            
    # 4.출력
    print(f"#{t+1} {max_fly}")


