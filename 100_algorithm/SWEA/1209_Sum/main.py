import sys
# open을 사용해서 input 파일을 연다
sys.stdin=open('input.txt')

# 이 문제는 10개의 TC를 가진다.
for _ in range(10):
    tc=input() # 테스트케이스 번호 입력 받음
    data=[list(map(int,input().split())) for _ in range(100)]
    #data=[] # 2차원 배열을 만들기 위한 리스트
    #for _ in range(100):
    #    tmp_list=list(map(int,input().split())) # 공백 기준으로 쪼개서 리스트로 만듦
    #    data.append(tmp_list) # 그 리스트를 data에 추가
    #print(data)

    # 초기 max값 세팅
    max_ans=0

    # 1. 각 행마다 가진 값들을 더한다.
    for arr in data:
        sum_arr=sum(arr)
        if sum_arr>max_ans:
            max_ans=sum_arr

    # 2. 각 열마다 가진 값들을 더한다.
    for i in range(100):
        tmp=0
        for j in range(100):
            tmp+=data[j][i]
        if tmp>max_ans:
            max_ans=tmp

    # 3. 대각선의 값들을 더한다.
    tmp1=0 #대각선값 1
    tmp2=0 #대각선값 2
    for i in range(100):
        tmp1+=data[i][i]
        tmp2+=data[i][100-i-1]
        if tmp1>max_ans:
            max_ans=tmp1
        if tmp2>max_ans:
            max_ans=tmp2

    # 4. 그 모든 값들 중 제일 큰 값을 구한다. -> max 금지
    print(f'#{tc} {max_ans}')
