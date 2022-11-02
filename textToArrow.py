"""
Copy and paste functionality for LaTex arrows. 
Copy the plain text arrow characters. Paste into a text file. On runtime, specify input(required) and output files in the command line (INCLUDING EXTENSIONS).
If no output file is specified, output printed to the command line. 
    Arrows are three specific unicode characters in order:
        chr(226) chr(8224) chr(8217)
Author: Jack Bosco (2022)
"""
from pyArgs import pyArgs
p = pyArgs(["in!", "out"])
p.parse()
f = open(p.getArgs()["in"], 'r')
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
if "out" in p.getArgs().keys():
    open(p.getArgs()["out"], 'w').write(ret)
else:
    print(ret)