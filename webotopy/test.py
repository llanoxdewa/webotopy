import re


result = re.search('(?<=Result:\s)\d+','Result: 100, and some else').group()
print(result)

