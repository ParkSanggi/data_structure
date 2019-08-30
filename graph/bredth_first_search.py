from queue import Queue

# vertex의 개수
n = 9
# 그래프
adjacent = []


# 너비 우선 탐색
# 인접한 vertex를 모두 방문한 후에 그와 인접한 vertex를 방문하는 방법
def breadth_first_search(start):
    q = Queue()
    # 사이클과 중복 방문을 막기 위해 방문 했던 vertex들을 표시
    visited = [False for _ in range(n)]

    q.put(start)
    visited[start] = True

    # queue에서 순서에 맞는 vertex를 꺼내서 방문 후 인접한 vertex들을 queue에 삽입한다.
    while not q.empty():
        vertex = q.get()
        print(vertex, end="  ")
        adjacent_list = adjacent[vertex]
        for u in adjacent_list:
            if not visited[u]:
                q.put(u)
                visited[u] = True
