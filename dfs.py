from collections import defaultdict

def dfs(graph, start):
  """
  Performs Depth-First Search on a graph

  Args:
      graph: A dictionary representing the graph. Keys are nodes, values are lists of neighboring nodes.
      start: The starting node for the DFS traversal.
  """
  visited = set()  # Keeps track of visited nodes

  def dfs_helper(node):
    visited.add(node)
    print(node, end=" ")  # Print the visited node
    for neighbor in graph[node]:
      if neighbor not in visited:
        dfs_helper(neighbor)

  dfs_helper(start)
  print()  # Newline after DFS traversal

def get_user_graph():
  """
  Prompts user for graph structure and returns it as a dictionary

  Returns:
      A dictionary representing the graph.
  """
  num_nodes = int(input("Enter the number of nodes in the graph: "))
  graph = defaultdict(list)  # Use defaultdict for flexibility

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
  start = input("Enter the starting node for DFS: ")
  dfs(graph, start)
