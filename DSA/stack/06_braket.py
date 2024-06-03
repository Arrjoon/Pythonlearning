def balanced(string):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    
    for char in string:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return not stack

if __name__ == "__main__":
    expr = "{()}[]"
    
    # Function call
    if balanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
