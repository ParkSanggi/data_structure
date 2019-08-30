n = 9
adjacent = []
visited = [False for _ in range(n)]


def depth_first_search(vertex):
    print(vertex, end="  ")
    visited[vertex] = True

    vertex_list = adjacent[vertex]
    for u in vertex_list:
        if not visited[u]:
            depth_first_search(u)

