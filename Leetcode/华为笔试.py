# 要依次经过车站[a,b,c],选择最佳乘车路线使得乘坐公交车总数最少，
# 输入：第一行有三个数字代表公交站，如[3,32,18],说明路线为从3号站点出发，途径32号，最终到达18号站点。第二行代表公交路线数量，后续每一行的数字第一个数字代表改公交线路的总站台数，剩余数字为公交线路经过站点的编号
# 公交线路单向循环，如[3, 2, 3, 7]代表有3个站点，路线为2,3，7
# from collections import defaultdict, deque
# import sys
# def func(start, end, routes):
#     station_to_routes = defaultdict(set)
#     for i, route in enumerate(routes):
#         for station in route:
#             station_to_routes[station].add(i)
#
#     queue = deque([(start, 0)])  # (当前站, 换乘次数)
#     visited_stations = set([start])  # 已访问的站
#     visited_routes = set()  # 已使用的线路
#
#     while queue:
#         current_station, changes = queue.popleft()
#
#         if current_station == end:
#             return changes
#
#         # 对于当前站，检查所有可用的线路
#         for route_id in station_to_routes[current_station]:
#             if route_id not in visited_routes:
#                 visited_routes.add(route_id)
#                 # 将此线路中的所有未访问过的站加入队列
#                 for next_station in routes[route_id]:
#                     if next_station not in visited_stations:
#                         visited_stations.add(next_station)
#                         queue.append((next_station, changes + 1))
#
#     return -1  # 如果无法到达终点站
    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().

# if __name__ == "__main__":
#     input = sys.stdin.read
#     data = input().splitlines()
#
#     # 解析输入
#     n, start, end = map(int, data[0].split())
#     num_routes = int(data[1])
#     routes = []
#
#     for line in data[2:]:
#         parts = list(map(int, line.split()))
#         routes.append(parts[1:])
#
#     # 调用函数
#     min  =  func(start, end, routes)
#     print(min)

# 给定整数n，和数组GRS[],其中n表示人数，数组GRS[][]是邻接表，GRS[i]的元素[a,b,c]代表员工i和员工a,b,c是同学或团队
# 将这n个人分成两组，使得每组不再有同学或团队的人
# 输入：数组形式的员工关系邻接表，第一行数字代表有N个顶点，顶点编号从0开始，后续接N行。第i行表示第i-1个顶点和他有关系的同学的顶点的编号
# 读取输入
# import sys
# from collections import defaultdict, deque
#
#
# def is_bipartite(n, grs):
#     colors = [0] * n  # 0: uncolored; 1: group A; -1: group B
#
#     def bfs(start):
#         queue = deque([start])
#         colors[start] = 1  # Start coloring with group A
#         while queue:
#             node = queue.popleft()
#             for neighbor in grs[node]:
#                 if colors[neighbor] == 0:  # If the neighbor is uncolored
#                     colors[neighbor] = -colors[node]  # Color it with the opposite color
#                     queue.append(neighbor)
#                 elif colors[neighbor] == colors[node]:  # If the neighbor has the same color
#                     return False
#         return True
#
#     for i in range(n):
#         if colors[i] == 0 and not bfs(i):  # If the node is uncolored and BFS fails
#             return False, []
#
#     # 分组结果
#     group_a = [i for i, color in enumerate(colors) if color == 1]
#     group_b = [i for i, color in enumerate(colors) if color == -1]
#
#     return True, (group_a, group_b)
#
#
#
#
# input = sys.stdin.read
# data = input().splitlines()
#
# # 解析输入
# n = int(data[0])
# grs = [[] for _ in range(n)]
#
# for i in range(1, n + 1):
#     neighbors = list(map(int, data[i].split()))
#     grs[i - 1] = neighbors
#
# # 调用函数
# possible, groups = is_bipartite(n, grs)
# if possible:
#     print("可以将这些人员分为两组：")
#     print("组A:", groups[0])
#     print("组B:", groups[1])
# else:
#     print("无法将这些人员分为两组，使得每组内没有同学或团队的关系。")
#
#
# from collections import defaultdict, deque

#
# def find_min_buses(start, end, routes):
#     # 建立车站到线路的映射
#     station_to_routes = defaultdict(set)
#     for i, route in enumerate(routes):
#         for station in route:
#             station_to_routes[station].add(i)
#
#     # BFS准备
#     queue = deque([(start, 0)])  # (当前站, 换乘次数)
#     visited_stations = set([start])  # 已访问的站
#     visited_routes = set()  # 已使用的线路
#
#     while queue:
#         current_station, changes = queue.popleft()
#
#         if current_station == end:
#             return changes
#
#         # 对于当前站，检查所有可用的线路
#         for route_id in station_to_routes[current_station]:
#             if route_id not in visited_routes:
#                 visited_routes.add(route_id)
#                 # 将此线路中的所有未访问过的站加入队列
#                 for next_station in routes[route_id]:
#                     if next_station not in visited_stations:
#                         visited_stations.add(next_station)
#                         queue.append((next_station, changes + 1))
#
#     return -1  # 如果无法到达终点站
#
#
# # 读取输入
# import sys
#
# input = sys.stdin.read
# data = input().splitlines()
#
# # 解析输入
# stations = list(map(int, data[0].split()))
# num_routes = int(data[1])
# routes = []
#
# for line in data[2:]:
#     parts = list(map(int, line.split()))
#     routes.append(parts[1:])
#
# # 找到从起点站到中间站，再从中间站到终点站的最少换乘次数
# start, mid, end = stations
# min_buses_start_mid = find_min_buses(start, mid, routes)
# min_buses_mid_end = find_min_buses(mid, end, routes)
#
# if min_buses_start_mid == -1 or min_buses_mid_end == -1:
#     print("无法到达终点站")
# else:
#     total_buses = min_buses_start_mid + min_buses_mid_end
#     print(f"最少需要乘坐 {total_buses} 次公交车")
#
# from collections import defaultdict, deque
#
#
# def build_graph(routes):
#     graph = defaultdict(list)
#     for i, route in enumerate(routes):
#         for j in range(len(route)):
#             current_station = route[j]
#             next_station = route[(j + 1) % len(route)]  # 单向循环
#             graph[current_station].append((next_station, i))
#     return graph
#
#
# def find_min_buses(graph, start, targets):
#     queue = deque([(start, 0, -1)])  # (当前站, 换乘次数, 当前线路)
#     visited = defaultdict(lambda: defaultdict(bool))  # visited[station][route] = True if visited
#     visited[start][-1] = True
#
#     while queue:
#         current_station, changes, current_route = queue.popleft()
#
#         if current_station in targets:
#             return changes
#
#         for next_station, next_route in graph[current_station]:
#             if not visited[next_station][next_route]:
#                 visited[next_station][next_route] = True
#                 if next_route != current_route:
#                     queue.append((next_station, changes + 1, next_route))
#                 else:
#                     queue.append((next_station, changes, next_route))
#
#     return -1  # 如果无法到达终点站
#
#
# # 读取输入
# import sys
#
# input = sys.stdin.read
# data = input().splitlines()
#
# # 解析输入
# stations = list(map(int, data[0].split()))
# num_routes = int(data[1])
# routes = []
#
# for line in data[2:]:
#     parts = list(map(int, line.split()))
#     routes.append(parts[1:])
#
# # 构建图
# graph = build_graph(routes)
#
# # 找到从起点站到中间站，再从中间站到终点站的最少换乘次数
# start, mid, end = stations
# min_buses_start_mid = find_min_buses(graph, start, {mid})
# min_buses_mid_end = find_min_buses(graph, mid, {end})
#
# if min_buses_start_mid == -1 or min_buses_mid_end == -1:
#     print("无法到达终点站")
# else:
#     total_buses = min_buses_start_mid + min_buses_mid_end
#     print(f"最少需要乘坐 {total_buses} 次公交车")

################################整理版###############################

# 1.https://mp.weixin.qq.com/s/ShP8sXYOVd_M62g1WKOvFQ
# 给定整数n，和数组GRS[],其中n表示人数，数组GRS[][]是邻接表，GRS[i]的元素[a,b,c]代表员工i和员工a,b,c是同学或团队
# 将这n个人分成两组，使得每组不再有同学或团队的人
# 输入：数组形式的员工关系邻接表，第一行数字代表有N个顶点，顶点编号从0开始，后续接N行。第i行表示第i-1个顶点和他有关系的同学的顶点的编号

from collections import defaultdict, deque


def is_bipartite(n, grs):
    colors = [0] * n  # 0: uncolored; 1: group A; -1: group B

    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with group A
        while queue:
            node = queue.popleft()
            for neighbor in grs[node]:
                if colors[neighbor] == 0:  # If the neighbor is uncolored
                    colors[neighbor] = -colors[node]  # Color it with the opposite color
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:  # If the neighbor has the same color
                    return False
        return True

    for i in range(n):
        if colors[i] == 0 and not bfs(i):  # If the node is uncolored and BFS fails
            return False, []

    # 分组结果
    group_a = [i for i, color in enumerate(colors) if color == 1]
    group_b = [i for i, color in enumerate(colors) if color == -1]

    return True, (group_a, group_b)


def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    grs = [[] for _ in range(n)]

    for i in range(1, n + 1):
        neighbors = list(map(int, data[i].split()))
        grs[i - 1] = neighbors

    return n, grs


if __name__ == "__main__":
    n, grs = read_input()
    possible, groups = is_bipartite(n, grs)

    if possible:
        print("可以将这些人员分为两组：")
        print("组A:", groups[0])
        print("组B:", groups[1])
    else:
        print("无法将这些人员分为两组，使得每组内没有同学或团队的关系。")

