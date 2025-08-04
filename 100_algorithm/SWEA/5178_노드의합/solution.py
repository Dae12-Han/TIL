#후위순회로 합 구하기
def postorder_sum(idx):
    if idx>N:
        return 0
    tree[idx]+=postorder_sum(idx*2)+postorder_sum(idx*2+1)
    return tree[idx]

T=int(input())
for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)
    for _ in range(M):
        node,value=map(int,input().split())
        tree[node]=value
    print('tree before',tree)
    postorder_sum(1)
    print('tree after',tree)
    print(f'#{tc} {tree[L]}')
