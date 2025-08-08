def find_subset(start,current_subset,current_sum):
    #현재 부분집합의 합이 target_sum
    if current_sum==target_sum:
        result.append(list(current_subset))
        return

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []

#필요한 인자들은?
#1.재귀를 중단시킬 파라미터(총합이 10이 되면 종료)
#2.누석해서 가야할 파라미터 -> 만들어지는 부분집합
#+그 선택할 집합의 index 파라미터
find_subset(start=0,current_subset=[],current_sum=0)
print(result)