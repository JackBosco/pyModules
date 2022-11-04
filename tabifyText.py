"""
Copy and paste functionality for LaTex to indent every line by 'space' spaces(\hspace{}). 
Copy the plain text. Paste into a text file. 
On runtime, specify input(required) and output files (INCLUDING EXTENSIONS) 
    as well as the number of spaces to indent in the command line.

args: in!, space!, out

If no output file is specified, output printed to the command line. 
Author: Jack Bosco (2022)
"""
def run(text, space):
    ret = ""
    for line in text.split('\n'):
        ret += "\hspace{" + str(space) + "ex}" + "\n"
        ret += line + '\n'
    return ret[:-1]

def main():
    from pyArgs import pyArgs
    p = pyArgs(["in!", "space!", "out"])
    p.parse()
    try:
        int(p.getArgs()["space"])
    except:
        raise ValueError("space arg :", p.getArgs()["space"], "must be an integer")
    f = open(p.getArgs()["in"], 'r').read()
    r = run(f, p.getArgs()["space"])
    if "out" in p.getArgs().keys():
        open(p.getArgs()["out"], 'w').write(r)
    else:
        print(r)

if __name__ == '__main__':
    main()