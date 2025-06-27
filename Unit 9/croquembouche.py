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

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    if not design:
        return []
    lst = [[design.val]]
    q = [design]
    vis = []
    while q:
        curr = q.pop(0)
        if not curr.left and not curr.right:
            continue
        if curr.left and not curr.right:
            lst.append([curr.left.val])
            q.append(curr.left)
        if curr.right and not curr.left:
            lst.append([curr.right.val])
            q.append(curr.right)        
        else:
            lst.append([curr.left.val, curr.right.val])
            q.append(curr.left)
            q.append(curr.right)
    return lst

def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []
    lst = [cupcakes.val]
    q = [(cupcakes, 0)]
    while q:
        curr, lvl = q.pop(0)
        if not curr.left and not curr.right:
            continue
        elif curr.left and not curr.right:
            lst.append(curr.left.val)
            q.append((curr.left, lvl+1))
        elif curr.right and not curr.left:
            lst.append(curr.right.val)
            q.append((curr.right, lvl+1))        
        else:
            if lvl % 2 == 0:
                lst.append(curr.right.val)
                lst.append(curr.left.val)   
            else:             
                lst.append(curr.left.val)
                lst.append(curr.right.val)
            q.append((curr.left, lvl+1))
            q.append((curr.right, lvl+1))
    return lst





croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(listify_design(croquembouche))

flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))

