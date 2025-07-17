# # def bidirectional_flights(flights):
# #     #0: {1,2}
# #     # 1: {0}
# #     # Make a dictionary 
# #     dict_flights = {}
# #     for i, flights in enumerate(flights):
# #         dict_flights[i] = {flight for flight in flights}

    
    
# #     for key, val in dict_flights.items():
# #       for value in val:
# #           if key not in dict_flights[value]:
# #               return False
          
# #     return True

# #             # num of elements in the flights1 list.
# #             # number of total nubmer
# #             # N/V number of nodes/vertices
# #             # E edges
# # flights1 = [[1, 2], [0], [0, 3], [2]]
# # # 0: 1, 2
# # # 1: 0
# # # etc.
# # # 1 
# # flights2 = [[1, 2], [], [0], [2]]


# # print(bidirectional_flights(flights1))
# # print(bidirectional_flights(flights2))
# # # Example Output:

# # # True
# # # False

# # # [[0 1]
# #     # [1 0] 
# #  # ]
# from collections import defaultdict
# def find_center(terminals):
#     # we can have a count dictionary where we store the number of times each number/terminal appears in the flights list, and we would return the maximum one, which is also the one that has a count equal to the length of the list
#     counter = defaultdict(int)
#     for terminal in terminals:
#         for n in terminal:
#             counter[n] += 1
    
#     max_count = 0
#     best_key = -1
#     for key, val in counter.items():
#         if val > max_count:
#             max_count = val
#             best_key = key

#     return best_key


# terminals1 = [[1,2],[2,3],[4,2]]
# terminals2 = [[1,2],[5,1],[1,3],[1,4]]

# print(find_center(terminals1))
# print(find_center(terminals2))
# # Example Output:

# 2
# 1

from collections import deque
def get_all_destinations(flights, start):
    seen = set(start)
    queue = deque(start)
    res = []

    while queue:
        node = queue.popleft()

        res.append(node)
        L = flights[node]
        print(L)
        for place in L:
            queue.append(place)
            seen.add(place)
        
    return res
    
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
# Example Output:

['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
'Reykjavik']
['Helsinki', 'Cairo', 'New York', 'Reykjavik']