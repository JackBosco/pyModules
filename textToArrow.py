from pyArgs import pyArgs

p = pyArgs(["in!", "out"])
p.parse()
if "in" in p.params:
    f = open(p.params["in"], 'r')
else:
    f = open("in.txt", 'r')
ret = ""
for line in f:
    while line[0] == ' ':
        line = line[1:]
    while len(line) > 0:
        if line[0] == '\n':
            line = line[1:]
            ret += "\\\\\n"
        elif len(line) >= 3 and ord(line[0]) == 226 \
            and ord(line[1]) == 8224 and ord(line[2]) == 8217:
            line = line[3:]
            ret += "$\\rightarrow$"
        else:
            ret += line[0]
            line = line[1:]
if "out" in p.params.keys():
    open(p.params["out"], 'w').write(ret)
else:
    print(ret)