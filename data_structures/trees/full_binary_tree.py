#  Every node has 0 or 2 children.

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)

    if self.root is None:
      self.root = new_node
      return

    current = self.root

    while True:
      # Check left first
      if value < current.value:
        if current.left is None:
          current.left = new_node
          return
        else:
          current = current.left
      # Check right after
      else:
        if current.right is None:
          current.right = new_node
          return
        else:
          current = current.right

def build_tree_node_list(values):
  tree = BinaryTree()

  for value in values:
    tree.insert(value)

  return tree

def preorder_traverse(node):
  """Root->Left->Right"""

  if node:
    print(f"{node.value}", end=" ")
    preorder_traverse(node.left)
    preorder_traverse(node.right)

values = [10, 5, 15, 3, 7, 12, 17]
tree = build_tree_node_list(values)
preorder_traverse(tree.root)
