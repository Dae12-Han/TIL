# 바이너리 카운팅을 통한 부분집합 생성
arr=[1,2,3]
n=len(arr)
subset_cnt=2**n
subsets=[] # 모든 부분집합을 담을 list

# 모든 경우의 수에 대해서 조회
# for i in range(subset_cnt):
for idx in range(1<<n):
    #print(idx)

    # 이번 경우의 수의 부분집합
    subset=[]
    for j in range(n): # j번째 요소가 이번의 경우의 수에 사용되었는지 판별
        '''
        idx=0 => 000
         j =0 => 000 & -> 0
         
        idx=3 => 011
         j =0 => 000 & -> True
         j =1 => 010 & -> True
        '''
        if idx & (1<<j):
            # j번째 요소가 이번 경우의 수에 사용되었음
            subset.append(arr[j])
    # 필요하다면, 이곳에 추가 조건을 ...
    if sum(subset)==3:
        subsets.append(subset)

print(subsets)

