#right,down만 확인하면 됌
dx=[1,0]
dy=[0,1]

def dfs(d,y,x,length):
    global max_length

    if d==0: #right
        visited=visited1

    if d==1: #down
        visited=visited2

    ny,nx=y+dy[d],x+dx[d]
    if 0<=nx<M and 0<=ny<N:
        if photo[ny][nx]==1 and not visited[ny][nx]:
            visited[ny][nx]=True
            dfs(d,ny,nx,length+1)

    max_length=max(max_length,length)
    return

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    photo=[list(map(int,input().split())) for _ in range(M)]
    max_length=0 #가장 긴 건축물

    #right 확인용
    visited1=[[False for _ in range(N)] for _ in range(M)]
    #down 확인용
    visited2=[[False for _ in range(N)] for _ in range(M)]

    for y in range(N):
        for x in range(M):
            if photo[y][x]==1:
                if not visited1[y][x]:
                    visited1[y][x]=True
                    dfs(0,y,x,1) #only right
                if not visited2[y][x]:
                    visited2[y][x]=True
                    dfs(1,y,x,1) #only down

    print(f'#{tc} {max_length}')