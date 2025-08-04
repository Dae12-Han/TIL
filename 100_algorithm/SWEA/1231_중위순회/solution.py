import sys
sys.stdin=open('input.txt')

def inorder(idx):
    if idx<=N:
        inorder(idx*2)
        print(tree[idx],end='')
        inorder(idx*2+1)

for tc in range(1,11):
    print(f'#{tc}',end=' ')
    N=int(input())
    tree=[None]*(N+1)
    for idx in range(N):
        input_data=list(input().split())
        root=int(input_data[0])
        value=input_data[1]
        tree[root]=value
    inorder(1)
    print()

