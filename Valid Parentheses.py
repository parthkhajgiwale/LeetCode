def is_valid(s):
    stack = []
    mappings = {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }
    
    for char in s:
        if char in mappings:
            top = stack.pop() if stack else '#'
            if top != mappings[char]:
                return False
        else:
            stack.append(char)
    return not stack

print(is_valid('(){}'))
