from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
    root = collection
    if root is None:
        return TreeNode(name)
    
    while root.right and root.left:
        if root.val > name:
            root = root.left
        elif root.val < name:
            root = root.right
        else:
            break
    
    if root.val > name:
        root.left = TreeNode(name)
    elif root.val <= name:
        root.right = TreeNode(name)

    
    return collection

def remove_plant(collection, name):
    root = collection
    
    while root.right and root.left:
        if root.val > name:
            root = root.left
        elif root.val < name:
            root = root.right
        else:
            break
    #it is found
    temp = root.left
    root.left = None
    temp2 = root.right
    root.right = None
    temp

    root = root.left
    root.left = None
    if root.val > name:
        root.left = TreeNode(name)
    elif root.val <= name:
        root.right = TreeNode(name)

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)
    
print_tree(add_plant(collection, "Aloe"))