from itertools import combinations

import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    Sij=[list(map(int,input().split())) for _ in range(N)]

    min_taste=float('inf')
    for comb in combinations(range(N),N//2):
        A=list(comb)
        B=[x for x in range(N) if x not in A]

        ta,tb=0,0
        for i in range(N//2):
            for j in range(N//2):
                if i==j:
                    pass
                else:
                    ta+=Sij[A[i]][A[j]]
                    tb+=Sij[B[i]][B[j]]

        min_taste=min(min_taste,abs(ta-tb))
    print(f'#{tc} {min_taste}')