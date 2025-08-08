dy=[0,0,-1,1]
dx=[-1,1,0,0]

def bfs(y,x):
    ans=0
    queue=[[y,x]]

    while queue:
        y,x=queue.pop(0)

        if matrix[y][x]==3:
            ans=1
            break

        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]

            if 0<=ny<16 and 0<=nx<16:
                if not visited[ny][nx] and matrix[ny][nx]!=1:
                    visited[ny][nx]=True
                    queue.append([ny,nx])  

    return ans

for _ in range(10):
    tc=int(input())
    matrix=[list(map(int,input())) for _ in range(16)]
    visited=[[False for _ in range(16)] for _ in range(16)]

    for y in range(16):
        for x in range(16):
            if matrix[y][x]==2:
                sy,sx=y,x

    visited[sy][sx]=True
    print(f'{tc} {bfs(sy,sx)}')