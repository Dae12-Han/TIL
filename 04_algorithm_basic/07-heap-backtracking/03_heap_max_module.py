import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

#음수로 구현해서 최대 힙으로 구현
max_heap=[]
for number in numbers:
    heapq.heappush(max_heap,-number)

print(max_heap)

#힙에서 가장 큰 요소를 제거하고 반환
largest=-heapq.heappop(max_heap)
print(largest)
