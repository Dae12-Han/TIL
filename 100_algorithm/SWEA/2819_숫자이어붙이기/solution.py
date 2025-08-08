dy=[0,0,-1,1]
dx=[-1,1,0,0]

def dfs(y,x,n):
    global numbers
    if len(n)==7:
        numbers.add(n)
        return

    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]

        if 0<=ny<4 and 0<=nx<4:
            dfs(ny,nx,n+matrix[ny][nx])

T=int(input())
for tc in range(1,T+1):
    #1.입력
    matrix=[list(input().split()) for _ in range(4)]
    numbers=set()

    for i in range(4):
        for j in range(4):
            dfs(i,j,matrix[i][j])

    print(f'{tc} {len(numbers)}')
