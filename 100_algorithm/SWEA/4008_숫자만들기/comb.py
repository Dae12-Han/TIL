
def dfs(level):
    global min_ans,max_ans

    if level>=N-1:
        print(comb)
        return
    
    for i in range(N-1):
        if used[i]==False:
            used[i]=True
            comb.append(op_list[i])
            comb.append(nums[i+1])
            dfs(level+1)
            used[i]=False
            comb.pop()
            comb.pop()

#1.입력
#N=int(input())
#op_cnt=list(map(int,input().split()))   #각 연산 개수
#nums=list(map(int,input().split())) #수식에 사용되는 숫자
N=5
cnt=[2, 1, 0, 1]
nums=[3, 5, 3, 7, 9]

op_list=['+']*cnt[0]+['-']*cnt[1]+['*']*cnt[2]+['/']*cnt[3]
comb=[nums[0]]
used=[False]*(N-1)


#2.자료형 정의 
#연산자 리스트를 미리 만들어둔다.

#print(op_list)
#최솟값,최대값 정의
min_ans,max_ans=100000000,-100000000

#3.동작 알고리즘
#dfs로 동작하게 한다
dfs(0)

#4.출력
print(max_ans-min_ans)