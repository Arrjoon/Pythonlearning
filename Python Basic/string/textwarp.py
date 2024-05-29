
def wrap(string, max_width):
    n=0
    for s in string:
        n=n+1
        text = "".join(s,end="")
        if n%max_width == 0:
            print("\n")
    return text

if __name__ == '__main__':
    string='abeFfdfabfddsfsdfsf'
    max_width = 4
    result = wrap(string, max_width)
    print(result)