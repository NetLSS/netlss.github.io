n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # cf. str은 iterable


def dfs(x, y):
    # 범위 검사
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

"""
map은 iterable의 각 요소가 함수를 적용하는 함수입니다. 기본적으로 str를 iterate하면 문자 하나하나로 쪼개지게 되고, 각 문자별로 int함수 결과를 취해주게 되죠.
"""

"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
