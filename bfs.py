from collections import deque

def bfs(graph, start):
  """
  Performs Breadth-First Search on a graph

  Args:
      graph: A dictionary representing the graph. Keys are nodes, values are lists of neighboring nodes.
      start: The starting node for the BFS traversal.

  Returns:
      A list containing the nodes visited in BFS order.
  """
  visited = set()  # Keeps track of visited nodes
  queue = deque([start])  # Queue for BFS traversal

  while queue:
    node = queue.popleft()
    visited.add(node)
    print(node, end=" ")  # Print the visited node

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)

  print()  # Newline after BFS traversal

def get_user_graph():
  """
  Prompts user for graph structure and returns it as a dictionary

  Returns:
      A dictionary representing the graph.
  """
  num_nodes = int(input("Enter the number of nodes in the graph: "))
  graph = {}

  for i in range(num_nodes):
    node = input("Enter node name: ")
    graph[node] = []

  print("Enter connections for each node (format: neighbor1 neighbor2 ...):")
  for node, neighbors in graph.items():
    connections = input(f"Connections for {node}: ").split()
    neighbors.extend(connections)

  return graph

if __name__ == "__main__":
  graph = get_user_graph()
  start = input("Enter the starting node for BFS: ")
  bfs(graph, start)

