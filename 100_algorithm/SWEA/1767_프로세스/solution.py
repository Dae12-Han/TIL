dx=[-1,1,0,0]
dy=[0,0,-1,1]

#간선 연결할 수 있는지/간 길 반환
def can_lay(d,y,x):
    ny,nx=y+dy[d],x+dx[d]
    wire_path=[]
    while 0<=nx<N and 0<=ny<N:
        if cells[ny][nx]!=0:
            return False,[]
        wire_path.append([ny,nx])
        ny+=dy[d]
        nx+=dx[d]
    return True,wire_path

#간선 연결
def lay_wire(path):
    for y,x in path:
        cells[y][x]=2 #전선 깔기

#간선 제거
def remove_wire(path):
    for y,x in path:
        cells[y][x]=0

def dfs(idx,cnt,length): #현재 코어 위치
    global max_cnt,min_len

    if idx==len(cores):
        if cnt>max_cnt: #가장 많이 연결된 경우일 때
            max_cnt=cnt
            min_len=length
        if cnt==max_cnt: #연결된 경우가 같을 때
            min_len=min(length,min_len)
        return #함수 종료

    for d in range(4): #4방 탐색
        okay,path=can_lay(d,cores[idx][0],cores[idx][1])
        if okay: #연결할 수 있으면
            lay_wire(path)    #간선 연결
            dfs(idx+1,cnt+1,length+len(path))
            remove_wire(path)  #간선 제거
    #연결하지 않은 경우
    dfs(idx+1,cnt,length)

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    cells=[list(map(int,input().split())) for _ in range(N)]

    #1.검사해야 할 셀을 저장한다
    cores=[]
    for r in range(1,N-1):
        for c in range(1,N-1):
            if cells[r][c]==1:
                cores.append([r,c])

    #정답 리스트
    max_cnt,min_len=0,0
    dfs(0,1,0) #idx:넘어가야할 인덱스,코어 수,전선 길이
    print(f'#{tc} {min_len}')