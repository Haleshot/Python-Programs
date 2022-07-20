# Breadth First Search Traversal program in Python
# Initializing a graph

from itertools import cycle

graph = {'0' : ['1', '2'], '1' : ['2'], '2': ['3'], '3' : ['1', '2']}

visited = [] # Visiting nodes List
queue = [] # Queue for nodes


# Function for BFS
def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, " - ", end = "")
            

        for adjacent in graph[m]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)


print("THE BFS Traversal is : ")
BFS(visited, graph, '0')