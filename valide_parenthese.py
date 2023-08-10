def isValid(s):
    stack=[]
    opening = '({['
    closing = ')}]'

    for x in s :
        if x in opening:
            stack.append(x)
        elif x in closing:
            if not stack:
                return False
            if opening.index(stack.pop())!= closing.index(x):
                return False

    return not stack

print(isValid("({[](){}})"))
