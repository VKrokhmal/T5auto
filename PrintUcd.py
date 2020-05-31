import re
#"      c7 b9 ad af   b2 ba ae bf   b1 bc a4 b1   ac b0 b1 ba  "
regex = re.compile(r'^\s{6}((([a-f]|[0-9])+).+[^\n])')
result=[]
hexs=[]
i = 0
with open('mer probe.txt') as data:
    for line in data:
        match = regex.search(line)
        if match:
            result.append(match.group(1))
#print(result)

for l in result:
    newline = l.strip().replace("  ","").replace("----","").split(" ")
    for x in newline:
        if x != "ff":
            q = int(x, 16)
            hexs.append(q)
            i=i+q

MER= i/len(hexs)/4
print(f"The MER value: {MER}")


