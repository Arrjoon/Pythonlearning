f = open("arjun.txt", "r")
content = f.read()
for line in content:
    print(line)
print(content)
f.close()
