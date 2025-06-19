def up_and_down(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count -= 1
        else:
            count += 1
    return count

lst = [1, 2, 3]
print(up_and_down(lst))

lst = [1, 3, 5]
print(up_and_down(lst))

lst = [2, 4, 10, 2]
print(up_and_down(lst))