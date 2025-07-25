T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    max_res=0

    if len(A)>len(B):
        A,B=B,A
    for i in range(len(B)-len(A)+1):
        ans=0
        for j in range(len(A)):
            ans+=(A[j]*B[i+j])
        max_res=max(ans,max_res)
    
    print(f"#{t} {max_res}")