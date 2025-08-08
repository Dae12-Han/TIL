def is_vaild_pos(board,row,col):
    for idx in range(row):
        if board[idx][col]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,n)):
        if board[i][j]==1:
            return False
    #모든 검증이 끝났는데 return False가 아니다?
    return True #이 위치에 퀸을 놓을 수 있다!

def n_queens(row,board):
    global cnt
    cnt+=1

    #row가 내 모든 행에 대해 조사를 했다면,,,
    if row==n:
        #어떤 일을 하고 종료
        return
    #아직 모든 행에 대해 조사하지 않았다면
    #모든 열에 대해서 현재 행에 퀸을 놓아 볼 것이다.
    for col in range(n):
        #현재 위치에 퀸을 놓아도 되는지 판별
        if is_vaild_pos(board,row,col): #True or False
            board[row][col]=1
            n_queens(row+1,board)
            board[row][col]=1

n = 4
board = [[0] * n for _ in range(n)]  # 4*4 2차원 배열 생성
solutions = []  # 모든 솔루션을 저장할 리스트
cnt=0

n_queens(0, board)

for solution in solutions:
    print(solution)
print(cnt)
