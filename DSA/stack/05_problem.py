#cheked balance brackets in expression


def balanced(string):
    stack =[]
    for i in string:
        if i in  ["(", "{", "["]:
            stack.append(i)
        else:
            if not stack:
                return False
            top_stack = stack.pop()
            if top_stack=='(':
                if i != ')':
                    return False
            

            if top_stack=='{':
                if i != '}':
                    return False
            
            if top_stack=='[':
                if i != ']':
                    return False
    
    if stack:
        return False
    return True
            

if __name__=="__main__":

    expr = "{()}[]"
 
    # Function call
    if balanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")