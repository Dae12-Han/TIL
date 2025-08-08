class MinHeap:
    def __init__(self):
        self.heap = []  # 힙을 저장할 빈 리스트 초기화
        self.length = 0  # 힙의 길이 초기화

    # 힙에 새로운 요소를 추가
    def heappush(self, item):
        self.heap.append(item)  # 새로운 요소를 리스트의 끝에 추가
        self.length += 1  # 힙의 길이 증가
        self._siftup(self.length-1) #가장 마지막에 삽입된 요소의 index를 넘긴다.

    # 힙에서 최소 요소를 제거하고 반환
    def heappop(self):
        if self.length == 0:
            raise IndexError("힙이 비었습니다.")  # 힙이 비어 있는 경우 예외 발생
        if self.length == 1:
            self.length -= 1
            return self.heap.pop()  # 힙에 요소가 하나만 있는 경우 그 요소를 반환
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._siftdown(0)
        return root
        
    # 주어진 리스트을 힙으로 변환
    def heapify(self, array):
        self.heap = array[:]  # 리스트의 복사본을 힙으로 사용
        n = len(array)
        for i in range(n//2-1,-1,-1):
            self._siftdown((i))

    # 삽입 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftup(self, idx):
        #마지막 삽입된 노드와 부모 노드의 크기를 비교
        #부모 노드의 인덱스를 얻어야한다.
        parent=(idx-1)//2
        while idx>0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx],self.heap[parent]=self.heap[parent],self.heap[idx]
            idx=parent
            parent=(idx-1)//2

    # 삭제 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftdown(self, idx):
        n=len(self.heap)
        largest=idx
        left=2*idx+1
        right=2*idx+2

        if left<n and self.heap[left]>self.heap[largest]:
            largest=left
        if right<n and self.heap[right]>self.heap[largest]:
            largest=right
        if largest!=idx:
            self.heap[idx],self.heap[largest]=self.heap[largest],self.heap[idx]
            self._siftdown(largest)

    def __str__(self):
        return str(self.heap)  # 힙의 문자열 표현 반환

min_heap = MinHeap()
min_heap.heappush(3)
min_heap.heappush(1)
min_heap.heappush(2)

print(min_heap)  # [1, 3, 2]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 3]

min_heap.heapify([5, 4, 3, 2, 1])
print(min_heap)  # [1, 2, 3, 5, 4]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 4, 3, 5] 
print(min_heap.heappop())  # 2
print(min_heap)  # [3, 4, 5]