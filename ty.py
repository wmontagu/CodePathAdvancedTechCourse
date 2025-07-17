from collections import deque

class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
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


def larger_order_tree(orders):
    # Do DFS inorder search
    # Starting with right and then going left
    # At each node, 

    if not orders:
        return None
    
    val = 0
    
    def helper(node):
        if not node:
            return
        helper(node.right)
        val += node.val
        node.val = val
        helper(node.left)
    node = orders
    helper(node)
    return orders
  

# """
#          4
#        /   \
#       /     \
#      1       21
#     / \     / \
#    0   2   26  15
#         \       \
#          3       8   
# """
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))
# Example Output:

# [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
# Explanation:
# Larger Order Tree:
#         30
#        /   \
#       /     \
#      36     21
#     / \     / \
#    36  35  26  15
#          \       \
#          33       8   