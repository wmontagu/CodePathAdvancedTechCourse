def is_nested_parens(paren_s):
    # use counter, if it ever ends under 0, then return false. increment up or down.
    
    def helper(paran, count):
        if count < 0:
            return False
        if count == 0 and not paran:
            return True
        if paran[0] == '(':
            count += 1
        elif paran[0] == ')':
            count -= 1
        print(paran[:1])
        return helper(paran[1:], count)
    return helper(paren_s, 0)


print(is_nested_parens('()'))