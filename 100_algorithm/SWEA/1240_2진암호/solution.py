import sys
# open을 사용해서 input 파일을 연다
sys.stdin=open('input.txt')

T=int(input()) #testcase
for tc in range(1,T+1):
    #1.입력
    N,M=map(int,input().split())
    arr=[list(map(int,input())) for _ in range(N)]
    
    #2.자료형 정의
    decode_list=[[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],
                 [0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

    #3.동작 알고리즘
    #3-1.암호 찾기
    #모든 암호 배열은 1로 끝남 -> 뒤로 순회하며 1을 발견하면 해당 배열을 기준으로 56자리 끊음
    find=False
    for row in arr:
        if find==True:
            break
        else:
            for col in range(M-1,-1,-1):
                if row[col]==1:
                    code=row[col-56+1:col+1] #암호코드
                    find=True
                    break
    #3-2.암호 해석
    odd_code,even_code=0,0
    for idx in range(8):
        code_7bit=code[idx*7:idx*7+7]
        for num in range(10):
            if code_7bit==decode_list[num]:
                if idx%2==0: #홀수 코드 계산->근데 여기서는 range 0부터 시작하니까
                    odd_code+=num
                else: even_code+=num #짝수 코드 계산
    #3-3.올바른 암호인가?
    if (odd_code*3+even_code)%10==0:
        #4.출력
        print(f'#{tc} {odd_code+even_code}')
    else:
        print(f'#{tc} 0')