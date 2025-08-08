import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

heapq.heapify(numbers)
print(numbers) #결과: [1, 3, 4, 10, 8, 7, 5]

heapq.heappush(numbers,-1)
print(numbers) #결과: [-1, 1, 4, 3, 8, 7, 5, 10]

smallest=heapq.heappop(numbers)
print(numbers) #결과:-1, 힙상태: [1, 3, 4, 10, 8, 7, 5]
