import re

text1 = "admin@kbtu.kz"
pattern = r"([a-z]+)@([a-z]+)\.([a-z]{2})"

res1 = re.match(pattern,text1)

print(res1.group(0))
print(res1.group(1))
print(res1.group(2))
print(res1.group(3))
