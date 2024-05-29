import re

txt = "my name is arjun"

x=re.findall("^my.*arjun$",txt)
print(x)