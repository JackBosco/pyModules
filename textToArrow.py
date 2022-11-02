"""
Copy and paste functionality for LaTex arrows. 
Copy the plain text arrow characters. Paste into a text file. 
On runtime, specify input(required) and output files in the command line (INCLUDING EXTENSIONS).

args: in!, out

If no output file is specified, output printed to the command line. 
    Arrows are three specific unicode characters in order:
        chr(226) chr(8224) chr(8217)
    OR one character:
        chr(8594)
    OR two characters:
        ->
Author: Jack Bosco (2022)
"""
def toArrows(text):
    ret = ""
    for line in text.split('\n'):
        while len(line) > 0:
            if len(line) >= 3 and ord(line[0]) == 226 \
                and ord(line[1]) == 8224 and ord(line[2]) == 8217:
                line = line[3:]
                ret += "$\\rightarrow$"
            elif ord(line[0]) == 8594:
                line = line[1:]
                ret += "$\\rightarrow$"
            elif len(line) >= 2 and line[:2] == '->':
                line = line[2:]
                ret += "$\\rightarrow$"
            elif len(line) >= 3 and line[:3] == '-->':
                line = line[3:]
                ret += "$\\Rightarrow$"
            else:
                ret += line[0]
                line = line[1:]
        ret += '\n'
    return ret[:-1]

def main():
    from pyArgs import pyArgs
    p = pyArgs(["in!", "out"])
    p.parse()
    f = open(p.getArgs()["in"], 'r').read()
    r = toArrows(f)
    if "out" in p.getArgs().keys():
        open(p.getArgs()["out"], 'w').write(r)
    else:
        print(r)

if __name__ == '__main__':
    main()