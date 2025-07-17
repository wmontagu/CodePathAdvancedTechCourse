# Problem 1: The Feeling is Mutual
def is_mutual(celebrities: list[list[int]]) -> bool:

# loop through row

    for i in range(1, len(celebrities)):
        for j in range(i, len(celebrities)-1):

    # for i in range(1, len(celebrities)):
    #     for j in range(0, i):
            if celebrities[i][j] != celebrities[j][i]:
                return False
            
    return True
#true

# [    0, 1, 1, 0]
# [1,     0, 1, 0]
# [1, 1,     0, 1]
# [0, 0, 1,     0]

celebrities1 = [
   [0, 1, 1, 0],
   [1, 0, 1, 0],
   [1, 1, 0, 1],
   [0, 0, 1, 0]
]

celebrities2 = [
   [0, 1, 1, 0],
   [1, 0, 0, 0],
   [1, 1, 0, 1],
   [0, 0, 0, 0]
]

# print(is_mutual(celebrities1))
# print(is_mutual(celebrities2))


# Problem 2: Network Lookup




def get_adj_matrix(clients):

    # map of the names
    # keep track of last index
    # make map of names: index
    index = 0
    names = {}
    for a, b in clients:
        if a not in names:
            names[a] = index
            index += 1
        if b not in names:
            names[b] = index
            index += 1
    size = len(names)
    # [0] * len(names)
    adj = [[0] * size for _ in range(size)]
    # iterate through clients
    for client in clients:
        # client: like ["Yalitza Aparicio", "Julio Torres"]
        i = names[client[0]]
        j = names[client[1]]
        adj[i][j] = 1
        adj[j][i] = 1
    
    return names, adj



clients = [
            ["Yalitza Aparicio", "Julio Torres"], 
            ["Julio Torres", "Fred Armisen"], 
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"], 
            ["Ali Wong", "Bowen Yang"]]

id_map, adj_matrix = get_adj_matrix(clients)
# print(id_map)
# print(adj_matrix)
# for r in adj_matrix:
#     print(r)


# {
#   'Fred Armisen': 0,
#   'Yalitza Aparicio': 1,
#   'Margaret Cho': 2,
#   'Bowen Yang': 3,
#   'Ali Wong': 4,
#   'Julio Torres': 5
# }

# [
#   [0, 0, 0, 0, 1, 1],  # Fred Armisen
#   [0, 0, 0, 0, 0, 1],  # Yalitza Aparicio
#   [0, 0, 0, 1, 1, 0],  # Margaret Cho
#   [0, 0, 1, 0, 1, 1],  # Bowen Yang
#   [1, 0, 1, 1, 0, 0],  # Ali Wong
#   [1, 1, 0, 1, 0, 0]   # Julio Torres
# ]

# Note: The order in which you assign IDs and consequently your adjacency matrix may look different


# Problem 1: Bacon Number
from collections import deque
def bacon_number(bacon_network: dict[str: list[str]], celeb: str) -> int:

    if celeb == 'Kevin Bacon':
        return 0
    
    bacon_queue = deque(["Kevin Bacon"])
    actor_queue = deque([celeb])
    bacon_seen = set()
    actor_seen = set()
    depth = 0
    while bacon_queue or actor_queue:
        depth += 1
        # bacon loop, pop elements of the length of the current queue
        n = len(bacon_queue)
        for _ in range(n):
            popped = bacon_queue.popleft()
            for name in bacon_network[popped]:
                bacon_seen.add(name)
                if name in actor_seen:
                    return depth
                if name not in bacon_seen:
                    bacon_queue.append(name)
                
        depth += 1
        # actor loop (then same thing here)
        n = len(actor_queue)
        for _ in range(n):
            popped = actor_queue.popleft()
            for name in bacon_network[popped]:
                actor_seen.add(name)
                if name in bacon_seen:
                    return depth
                if name not in actor_seen:
                    actor_queue.append(name)
            
    return -1 # not inside at all
    
    # hopefully that works
    # time: idk
    # space: O(N)?


    # bacon_q
    # celeb_q

    # bacon_seen: set
    # celeb_seen: set
    
    #   if you see something while doing bfs in bacon that is in the celeb_seen, return depth
    #   if you see something while doing bfs in celeb that is in the bacon_seen, return depth
    


bacon_network = {
    "Kevin Bacon": ["Kyra Sedgewick", "Forest Whitaker", "Julia Roberts", "Tom Cruise"],
    "Kyra Sedgewick": ["Kevin Bacon"],
    "Tom Cruise": ["Kevin Bacon", "Kyra Sedgewick"],
    "Forest Whitaker": ["Kevin Bacon", "Denzel Washington"],
    "Denzel Washington": ["Forest Whitaker", "Julia Roberts"],
    "Julia Roberts": ["Denzel Washington", "Kevin Bacon", "George Clooney"],
    "George Clooney": ["Julia Roberts", "Vera Farmiga"],
    "Vera Farmiga": ["George Clooney", "Max Theriot"],
    "Max Theriot": ["Vera Farmiga", "Jennifer Lawrence"],
    "Jennifer Lawrence": ["Max Theriot"]
}

print(bacon_number(bacon_network, "Jennifer Lawrence"))
print(bacon_number(bacon_network, "Tom Cruise"))

# 5
# 1


