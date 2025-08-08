import sys
sys.stdin=open('input.txt')


def dfs(level,res):
    global min_ans,max_ans

    if level>=N-1:
        min_ans=min(res,min_ans)
        max_ans=max(res,max_ans)
        return
    
    if cnt[0]>0: 
        cnt[0]-=1
        dfs(level+1,res+nums[level+1])
        cnt[0]+=1

    if cnt[1]>0: 
        cnt[1]-=1
        dfs(level+1,res-nums[level+1])
        cnt[1]+=1

    if cnt[2]>0: 
        cnt[2]-=1
        dfs(level+1,res*nums[level+1])
        cnt[2]+=1

    if cnt[3]>0: 
        cnt[3]-=1
        if res<0:
            tmp=-(-res//nums[level+1])
        else: tmp=res//nums[level+1]
        dfs(level+1,tmp)
        cnt[3]+=1

T=int(input())
for tc in range(1,T+1):
    #1.입력
    N=int(input())
    cnt=list(map(int,input().split()))   #각 연산 개수
    nums=list(map(int,input().split())) #수식에 사용되는 숫자

    #2.자료형 정의 
    min_ans,max_ans=100000000,-100000000 #최솟값,최대값 정의

    #3.동작 알고리즘
    #dfs로 동작하게 한다
    dfs(0,nums[0])

    #4.출력
    print(f'#{tc} {max_ans-min_ans}')