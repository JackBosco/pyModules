"""
Copy and paste functionality for LaTex newlines (\\). 
Copy the plain text. Paste into a text file. 
On runtime, specify input(required) and output files in the command line (INCLUDING EXTENSIONS).

args: in!, out

If no output file is specified, output printed to the command line. 
Author: Jack Bosco (2022)
"""
def newLines(text):
    ret = ""
    for line in text.split("\n"):
        while len(line) > 0 and line[0] == ' ':
            line = line[1:]
        if len(line) != 0:
            ret += line + "\\\\\n"
    return ret[:-1]

def main():
    from pyArgs import pyArgs
    p = pyArgs(["in!", "out"])
    p.parse()
    f = open(p.getArgs()["in"], 'r').read()
    r = newLines(f)
    if "out" in p.getArgs().keys():
        open(p.getArgs()["out"], 'w').write(r)
    else:
        print(r)

if __name__ == '__main__':
    main()