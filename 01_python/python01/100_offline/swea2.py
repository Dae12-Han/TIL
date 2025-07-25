T=int(input())
for t in range(1,T+1):
    #1.입력
    N=int(input())
    matrix=[list(map(int,input().split())) for _ in range(N)]
    #2.자료형 정의
    #3.동작함수
    print(f"#{t}")
    for i in range(N):
        degree_90,degree_180,degree_270='','',''
        for j in range(N):
            degree_90+=str(matrix[N-j-1][i])
            degree_180+=str(matrix[N-i-1][N-j-1])
            degree_270+=str(matrix[j][N-i-1])
        print(degree_90+" "+degree_180+" "+degree_270)

    #4.출력