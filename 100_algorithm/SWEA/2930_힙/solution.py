dx=[+1,-1,-1,+1]
dy=[+1,+1,-1,-1]

def tour(d,y,x,cnt): #dr->direction:무조건 0,1,2,3 방향으로 가야하지 사각형으로 만들어짐
    #test=[[0 for _ in range(N)] for _ in range(N)]
    #test[y][x]=1
    #for t in test:
    #    print(t)
    #print()
    global ans

    for k in range(d,d+2): #현재 방향으로 쭉 갈 것인가, 아니면 다음 방향으로 갈 것인가? => 2가지 선택지 밖에 없음
        if k==4:
            break

        ny=y+dy[k]
        nx=x+dx[k]

        if 0<=ny<N and 0<=nx<N:
            #만약에 원점으로 돌아온다면
            if ny==j and nx==i:
                #print("투어 완료!",dessert,"cnt:",cnt)
                ans=max(ans,cnt)
                return

            if cafes[ny][nx] not in dessert:
                if not visited[ny][nx]:
                    dessert.add(cafes[ny][nx])
                    visited[ny][nx]=True
                    #print("direction:",k,"before:",y,x,"after:",ny,nx,"cnt:",cnt)
                    tour(k,ny,nx,cnt+1)
                    dessert.remove(cafes[ny][nx])
                    visited[ny][nx]=False
    return -1

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    cafes=[list(map(int,input().split())) for _ in range(N)]

    ans=-1
    dessert=set()
    for j in range(N): #가장자리 제외
        for i in range(N):
            dessert = set()
            dessert.add(cafes[j][i])
            visited=[[False for _ in range(N)] for _ in range(N)]
            visited[j][i]=True
            #ans=max(ans,tour(0,j,i,1))
            tour(0,j,i,1)
    print(f'#{tc} {ans}')