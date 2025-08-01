import sys
sys.stdin=open('input.txt')

for tc in range(1,11):
    N=int(input())
    arr=input()

    #중위표기식->후위표기식
    post,operator=[],[] #
    for n in range(N):
        if arr[n]=='+':
            operator.append('+')
        else: #숫자일 때
            post.append(int(arr[n]))

            if operator:
                post.append(operator.pop())

    #후위표기식 계산하기
    stack=[]
    for p in post:
        if p=='+':
            a=stack.pop()
            b=stack.pop()
            result=(a+b)
            stack.append(result)
        else:
            stack.append(p)

    print(f'#{tc} {result}')