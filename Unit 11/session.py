# def can_move_safely(position, grid):
#     seen = set()

#     def dfs(i, j):
#         if (i,j) in seen or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 and not (position[1] == j and position[0] == i):
#             return False
#         if i == len(grid) - 1 and j == len(grid) - 1:
#             return True
        
#         seen.add((i,j))
#         return dfs(i - 1, j) or dfs(i + 1, j) or dfs(i, j - 1) or dfs(i, j + 1)
    
#     return dfs(position[0], position[1])

#     # base case: [i]j] is out of bounds. if the value at the positon is 0, then we also return
#     # add t oseen set
#     # 
# # Example Usage:

# grid = [
#     [1, 0, 1, 1, 0], # Row 0
#     [1, 1, 1, 1, 0], # Row 1
#     [0, 0, 1, 1, 0], # Row 2
#     [1, 0, 1, 1, 1]  # Row 3
# ]

# position_1 = (0, 0)
# position_2 = (0, 4)
# position_3 = (3, 0)

# print(can_move_safely(position_1, grid))
# print(can_move_safely(position_2, grid))
# print(can_move_safely(position_3, grid))
# # Example Output:

# # True
# # Example 1 Explanation: Can follow the path (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
# # (2, 2) -> (3, 2) -> (3, 3) -> (3, 4)

# # True
# # Example 2 Explanation: Although we start in an unsafe position, we can immediately
# # arrive in a safe position and from there safely travel to the bottom right corner (3, 4).

# # False

# # 1,0
# # | 
# #  2,0, 1,1
# #  |
# #  2,1 , 1,2
 

# #  1,2
# #  |

def list_all_escape_routes(grid):
    seen = set()
    escape_routes = set()

    def dfs(i, j):
        if (i == len(grid) - 1 and j == len(grid) - 1) or (i, j) in escape_routes:
            return True
        if (i,j) in seen or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return False
        
        seen.add((i,j))
        escape_routes.add((i,j))
        if dfs(i - 1, j) or dfs(i + 1, j) or dfs(i, j - 1) or dfs(i, j + 1):
            return True
        else:
            escape_routes.remove((i,j))
            return False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if dfs(i, j):
                    escape_routes.add((i, j))
                
    
    # loop through each position in the matrix and run a dfs function on it.
    # have a 2 sets. One for storing all nodes you visited, and one for nodes that you know will return True
    # 
    return list(escape_routes)

grid = [
    [1, 0, 1, 0, 1], # Row 0
    [1, 1, 1, 1, 0], # Row 1
    [0, 0, 1, 0, 0], # Row 2
    [1, 0, 1, 1, 1]  # Row 3
]

print(list_all_escape_routes(grid))
# Example Output:

# [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]


