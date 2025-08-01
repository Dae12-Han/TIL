def fibonacci_memoization(n):
    #n이 2 이상이고, memo[n]번째가 아직 계산되지 않았으면
    if n>=2 and memo[n]==0:
        memo[n]=fibonacci_memoization(n-1)+fibonacci_memoization(n-2)
    return  memo[n]

n=10
# 10개의 값 기록 list
memo=[0]*(n+1) #0부터 10까지니까 총 11개

memo[0],memo[1]=0,1
print(fibonacci_memoization(n))