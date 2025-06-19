
def can_split_coffee(coffee, n):
    S = sum(coffee)
    if S % n == 0:
        return True
    return False


def helper(coffee):
    return coffee[0] + helper(coffee[1:])
def can_split_coffee(coffee, n):
    sum = helper()
    return sum % n == 0
