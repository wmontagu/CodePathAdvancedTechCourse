
def map_chambers(sections):
    def helper(sections):
        if len(sections) == 1:
            return sections[0]
        return {sections[0]: helper(sections[1])}
        
    return helper(sections)
# sections = ["Atlantis", ["Coral Cave", ["Pearl Chamber"]]]
# print(map_chambers(sections))


def longest_trident_sequence(gems):
    longest = 0
    curr = 1
    for i in range(1, len(gems)):
        if gems[i] - gems[i-1] == 1:
            curr += 1
        else:
            longest = max(longest, curr)
            curr = 1
    return max(longest, curr)


# def longest_trident_sequence_recursive(gems):
#     longest = 0
#     def helper(index, longest):
#         # if index == len(gems) - 1:
#         #     return gems[index]
#         if gems[index] == (gems[index - 1] + 1):
#             return helper(index + 1, longest)return 1 + 
#         return gems[index] + helper(index + 1, longest)

#     helper(1, 0)
    
# # print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
# # print(longest_trident_sequence([5, 10, 7, 8, 1, 2]))
    # # # # 
    
# 5
# Example 1 Explanation: longest sequence is 2, 3, 4, 5, 6

# 2
# Example 2 Explanation: longest sequence is 7, 8 or 1, 2


def find_last_building(n, k):
    return find_last_building_helper(n, k) + 1  # Adjust for 1-based indexing

def find_last_building_helper(n, k):
    if n == 1:
        return 0  # Base case: the last building standing is at position 0 (0-based index)
    
    return (find_last_building_helper(n - 1, k) + k) % n

print(find_last_building(5, 2))
print(find_last_building(6, 5))


# def find_last_building(n, k):
#     pass

# print(find_last_building(5, 2))
# print(find_last_building(6, 5))