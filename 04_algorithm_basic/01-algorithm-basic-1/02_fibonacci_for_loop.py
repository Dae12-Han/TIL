def fibonacci_for_loop(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    # n이 2 이상인 경우
    else:
        first,second=0,1  # fib(i-1),fib(i-2)의 역할을 해 줄 것
        for _ in range(2,n+1):
            #다음 피보나치 수는 이전 두 항의 합을 사용한다.
            next_fib=first+second
            first,second=second,next_fib
    return second

# 사용 예시
print(fibonacci_for_loop(10)) # 55