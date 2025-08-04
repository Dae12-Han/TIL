```python
import sys
sys.stdin=open('input.txt')

#parent는 항상 사칙연산
#child는 숫자

#2.동작 알고리즘
def cal(root): #사칙연산 함수
    if root<=N:
        #2-1.숫자라면 return
        if tree[root].isdigit():
            return tree[root]
        #2-2.루트가 사칙연산이라면 -> 자식 노드로 가야함
        else:
            left_child=cal(root*2)
            right_child=cal(root*2+1)
            #print(f'root {tree[root]} left {left_child} right {right_child}')
            #사칙연산 계산하기
            if tree[root] == '+': return int(left_child) + int(right_child)
            elif tree[root] == '-': return int(left_child) - int(right_child)
            elif tree[root] == '*': return int(left_child) * int(right_child)
            elif tree[root] == '/': return int(left_child) // int(right_child)

for tc in range(1,11):
    #1.입력
    N=int(input())
    tree=[None]*(N+1)
    for _ in range(N):
        input_data=list(input().split())
        idx=int(input_data[0])
        tree[idx]=input_data[1]
    #print(tree)
    print(f'#{tc}',cal(1))
``` 
# 해당 코드가 에러 나는 이유
좋아요. 이 코드가 틀리거나 터지는 대표 **반례 3가지**를 드릴게요. (입력 형식은 SWEA 사칙연산 트리처럼 `idx 값 [왼쪽 오른쪽]`이 오지만, 당신 코드가 두 번째 토큰만 쓰므로 그대로 넣어도 동작합니다.)

---

### 1) 완전 이진트리가 아닌 경우 (자식 인덱스가 2*i, 2*i+1이 아님)

당신 코드는 자식을 **무조건** `idx*2`, `idx*2+1`로 내려가지만, 실제 입력은 임의의 자식 인덱스를 가질 수 있어요.

```
4
1 + 2 4
2 3
3 100
4 7
```

* **정답 의도**: 1번 노드(+)의 자식은 2와 4 → 3 + 7 = **10**
* **당신 코드**: 1의 자식을 2와 3으로 고정 → 3 + 100 = **103** (오답)

---

### 2) 음수 리프 값 (isdigit 실패)

`'-5'.isdigit()`는 `False`라서, 숫자인데도 연산자로 오인하고 재귀를 내려가 **에러**가 납니다.

```
3
1 + 2 3
2 -5
3 2
```

* **정답**: (-5) + 2 = **-3**
* **당신 코드**: 2번 노드를 연산자로 보고 `cal(4)`, `cal(5)` 호출 → 범위 밖 → `None` 반환 → `int(None)`에서 **TypeError** 발생

---

### 3) 소수(실수) 리프 값 (isdigit 실패)

`'3.5'.isdigit()`도 `False`라서 같은 문제.

```
3
1 + 2 3
2 3.5
3 2
```

* **정답**: 3.5 + 2 = **5.5** (혹은 문제에서 정수만 허용이면 입력 자체가 잘못된 것)
* **당신 코드**: 2번을 연산자로 착각 → 자식 재귀 → **에러**

---

### 왜 생기나?

* 자식 인덱스를 **입력대로 저장**하지 않고, 완전 이진트리 규칙(2\*i)을 가정.
* 숫자 판별을 `str.isdigit()`에 의존 → **음수/실수**는 False.
* (추가) 실제 SWEA 포맷에서는 **연산자 노드가 자식 인덱스를 갖고**, **숫자 노드는 값만** 갖습니다. 따라서 자료구조를 `(op, left, right)` 또는 `int`로 구분해 저장해야 합니다.
