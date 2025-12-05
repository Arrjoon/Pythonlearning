s = 'malayalam'

i,j = 0,len(s)-1
is_plaindrome =True
while(i<j):
    if s[i] != s[j]:
        is_plaindrome = False

    j=j-1
    i=i+1


if is_plaindrome:
    print('yes')
else:
    print("No")
    