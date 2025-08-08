import sys
sys.stdin = open("input.txt")

def combination(arr,r):
    result=[]

    if r==1: #선택할 요소가 1개만 남은 경우
        #남아있는 arr의 모든 각 값들을 배열로 만들어서 반환
        return [[i] for i in arr]
    for idx in range(len(arr)):
        elem=arr[idx]
        for rest in combination(arr[idx+1:],r-1):
            result.append([elem]+rest)
    return result

T = int(input())
for tc in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력 받아 리스트로 저장
    arr = list(map(int, input().split()))

    # 직원당 키는 최대 10000이므로, 최대 높이는 10000 * N
    min_height = 10000 * N 
    #1명부터 N명까지 만들 수 있는 모든 키의 조합
    for r in range(1,N+1):
        #조합을 통해 얻어낸 리스트를 순회해서
        for comb in combination(arr,r):
            #조합에 들어온 모든 점원들의 키를 합한 경우
            total=sum(comb)
            #최종조건:선반보다는 키의 합이 커야한다.
            if total>=B:
                #근데, 그 중에 제일 작아야한다
                min_height=min(min_height,total)

    # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
    print(f"#{tc} {min_height - B}")

