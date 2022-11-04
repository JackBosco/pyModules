from pyArgs import pyArgs
import textToArrow as t2a
import addNewLine as aNL
import tabifyText as tab
"""
Args:
    in! :  input file with extension (required)
    first! : first algorithm to transform input (required)
             (options are textToArrow : t2a, addNewLine : aNL, tabifyText: tab)
    second : second algorithm to transform input 
             (options are textToArrow : t2a, addNewLine : aNL, tabifyText : tab)
    third  : third algorithm to transform input 
             (options are textToArrow : t2a, addNewLine : aNL, tabifyText : tab)
    out : out file
"""
def runTabLen(r):
    if 'spaces' in p.getArgs().keys():
        try:
            spaces = int(p.getArgs()['spaces'])
        except:
            raise ValueError("space arg :", p.getArgs()["spaces"], "must be an integer")
    else:
        spaces = 4
    return tab.run(r, spaces)

funcs = {"t2a" : t2a, "aNL" : aNL, "tab":tab}
p = pyArgs(["in!", "first!", "second", "third", "out", "spaces"])
p.parse()
f = open(p.getArgs()["in"], 'r').read()

keys = p.getArgs().keys()
for label in ["first", "second", "third"]:
    if label in keys:
        if p.getArgs()[label] == "tab":
            f = runTabLen(f)
        else:
            f = funcs[p.getArgs()[label]].run(f)

if "out" in p.getArgs().keys():
    open(p.getArgs()["out"], 'w').write(f)
else:
    print(f)