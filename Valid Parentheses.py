def isValid(s):
    stack = []

    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # If opening bracket, push it
        if char in "({[":
            stack.append(char)

        # If closing bracket, check the top of stack
        else:
            if not stack or stack[-1] != matching[char]:
                return False

            stack.pop()

    # Stack should be empty if all brackets matched
    return len(stack) == 0


# Examples
print(isValid("({[]})"))  # True
print(isValid("([)]"))    # False
print(isValid("((())"))   # False
