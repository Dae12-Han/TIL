def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

# 구하고자 하는 값 N
N=5
# 최종 결과값
answer=1
# 이제부터 1부터 N까지 answer에 곱해 나갈 수 있도록 순회
for num in range(1,N+1):
    answer*=num
print(answer)