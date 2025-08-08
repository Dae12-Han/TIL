def depth_first_search(vertex):
    '''
        vertex:현재 방문 정점
    '''
    #visited를 global 처리해야할까? 안 그래도 됌!
    # --왜?--> 메모리 상에 idx를 찾아가는거이기 때문에 괜찮음
    #글로벌에 있는 visited를 사용하겠다 명시
    global visited #안 적어도 되긴 함.
    
    #정점 방문
    print(graph[vertex])
    visited[vertex]=True

    #현재 정점이 진출 할 수 있을, 후보군을 찾는다!
    #인접 행렬의 vertex번째 리스트를 순회한다.
    for idx in range(N):
        if adj_matrix[vertex][idx] and visited[idx]==False:
            visited[vertex]=True
            depth_first_search(idx)

        # 0    1    2    3    4    5    6
graph = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# 정점 수: N
N = 7
#해당 정점 방문 여부 표시:False로 초기화
visited=[False]*N
# 인접 행렬
adj_matrix = [
#    A  B  C  D  E  F  G
    [0, 1, 1, 0, 0, 0, 0], # A
    [1, 0, 0, 1, 1, 0, 0], # B
    [1, 0, 0, 0, 1, 0, 0], # C
    [0, 1, 0, 0, 0, 1, 0], # D
    [0, 1, 1, 0, 0, 1, 0], # E
    [0, 0, 0, 0, 1, 0, 1], # F
    [0, 0, 0, 0, 0, 1, 0], # G
]

#시작 정점을 0번인 A부터 시작
depth_first_search(0)

