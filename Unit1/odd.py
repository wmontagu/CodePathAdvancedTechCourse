def get_odds(nums):
    res = []
    for num in nums:
        if num % 2 == 1:
            res.append(num)
    return res

nums = [1, 2, 3, 4]
print(get_odds(nums))

nums = [2, 4, 6, 8]
print(get_odds(nums))