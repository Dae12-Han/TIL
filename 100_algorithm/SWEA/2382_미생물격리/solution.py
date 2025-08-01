import sys
sys.stdin=open('sample.txt')

# 상: 1, 하: 2, 좌: 3, 우: 4
dx=[0,0,0,-1,1]
dy=[0,-1,1,0,0]

def microbe(y,x,num,dir):
    #다음 셀로 이동
    ny=y+dy[dir]
    nx=x+dx[dir]

    #만약 이동한 위치가 셀 약품이 칠해진 곳이라면
    if ny==0 or nx==0 or ny==N-1 or nx==N-1:
        #1.미생물 수 반으로 줄이기
        nnum=num//2
        if nnum==0: #만약 죽었으면... 포함하지 않음
            return
        else:
            #2.위치 바꾸기
            if dir==1: ndir=2
            elif dir==2: ndir=1
            elif dir==3: ndir=4
            else: ndir=3
    else:
        nnum=num
        ndir=dir

    return [ny,nx,nnum,ndir]
        
T=int(input()) #테스트케이스
for tc in range(1,T+1):
    N,M,K=map(int,input().split()) #N: 셀 갯수, M: 격리 시간, K: 군집 갯수
    cell=[list(map(int,input().split())) for _ in range(K)]

    for _ in range(M): # M초만큼 시간이 흐른다..
        ncell=[] #새로운 리스트(미생물 정보)

        for c in cell: # K군집들이 이동한다..
            y,x,num,dir=c
            nk=microbe(y,x,num,dir)

            #죽으면 pass
            if not nk:
                pass

            ncell.append(nk)

        '''
        여기서 틀림!
        '''
        #군집 합치기:ncell순회>tmp순회
        tmp_list=[] #임시로 저장할 리스트
        for nc in ncell:
            if not tmp_list:
                tmp_list.append(nc)
            else:
                for i in range(len(tmp_list)):
                    if nc[0]==tmp_list[i][0] and nc[1]==tmp_list[i][1]:
                        if nc[2]>tmp_list[i][2]:
                            tmp_list[i]=[nc[0],nc[1],nc[2]+tmp_list[i][2],nc[3]]
                        else:
                            tmp_list[i]=[tmp_list[i][0],tmp_list[i][1],nc[2]+tmp_list[i][2],tmp_list[i][3]]
                    else:
                        tmp_list.append(nc)
            #print(f'{tmp_list}')

        cell=tmp_list

    #print(cell)
    print(f'#{tc} {sum([cell[i][2] for i in range(len(cell))])}')