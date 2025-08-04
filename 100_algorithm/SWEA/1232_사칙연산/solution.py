import sys
sys.stdin=open('input.txt')

def cal(idx):
    kind=tree[idx][0] #종류
    if kind=='num':
        return tree[idx][1]
    else:
        _,op,l,r=tree[idx]
        lc=cal(l)
        rc=cal(r)
        if op=='+': return lc+rc
        if op=='-': return lc-rc
        if op=='*': return lc*rc
        if op=='/': return lc//rc

for tc in range(1,11):
    N=int(input())
    tree=[None]*(N+1)
    for _ in range(N):
        input_data=list(input().split())
        idx=int(input_data[0])
        if input_data[1] in '+-*/':
            tree[idx]=['op',input_data[1],int(input_data[2]),int(input_data[3])]
        else:
            tree[idx]=['num',int(input_data[1])]
    print(f'#{tc} {cal(1)}')