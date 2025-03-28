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
      if value < current.value:
        if current.left is None:
          current.left = new_node
          return
        else:
           current = current.left
      else:
        if current.right is None:
          current.right = new_node
          return
        else:
            current = current.right
    
  def grow_tree(self, values):
    if values:
      for value in values:
          self.insert(value)
  
  def traverse(self, option, node=None, nodes=None):
    """1 = preorder, 2 = inorder, 3 = postorder"""
      
    valid_options = {1, 2, 3}
    
    if option not in valid_options:
      print(f"Selected option is not valid", end="")
    
    if nodes is None:
      nodes = []
        
    if node:
      if option == 1: #Preorder traverse
        nodes.append(node.value)
        self.traverse(option, node.left, nodes)
        self.traverse(option, node.right, nodes)
      if option == 2: #Inorder traverse
        self.traverse(option, node.left, nodes)
        nodes.append(node.value)
        self.traverse(option, node.right, nodes)
      if option == 3: #Postorder traverse
        self.traverse(option, node.left, nodes)
        nodes.append(node.value)
        self.traverse(option, node.right, nodes)

    return nodes

  def validate_bst(self, node, min_val=float("-inf"), max_val=float("inf")):

    if node is None:
        return True

    if not(min_val < node.value < max_val):
        return False

    return(self.validate_bst(node.left, min_val, node.value) and
        self.validate_bst(node.right, node.value, max_val)
    )

  def get_lca(self, node, val_a, val_b):

    if node is None:
      return False

    if node.value == val_a or node.value == val_b:
      return node

    left_lca = self.get_lca(node.left, val_a, val_b)
    right_lca = self.get_lca(node.right, val_a, val_b)

    if left_lca and right_lca:
      return node

    return left_lca if left_lca else right_lca

  def deserialize(self, values):
    if not values or values[0] == "null":
      return None

    self.root = Node(int(values[0]))
    queue = [self.root]
    i = 1

    while i < len(values):
      current = queue.pop(0)

      if i < len(values) and  values[i] != 'null':
        current.left = Node(int(values[i]))
        queue.append(current.left)
      i += 1

      if i < len(values) and  values[i] != 'null':
        current.right = Node(int(values[i]))
        queue.append(current.right)
      i += 1

      return self.root

values = [8, 3, 10, 1, 6, 14]
tree = BinaryTree()
tree.grow_tree(values)

# Preorder traversal
preorder_list = tree.traverse(1, tree.root)
print(f"Preorder: {preorder_list}")

# Inorder traversal on the same tree (no need to rebuild)
inorder_list = tree.traverse(2, tree.root)
print(f"Inorder: {inorder_list}")