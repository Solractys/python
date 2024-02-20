s = "(){})("
def isValid(s: str) -> bool:
    stack = []
    for l in s:
        if l in '([{' :
            stack.append(l)
        else:
            if not stack or \
                (l == ')' and stack[-1] != '(') or \
                (l == '}' and stack[-1] != '{') or \
                (l == ']' and stack[-1] != '['):
                return False
            stack.pop()
    return not stack
print(isValid(s))