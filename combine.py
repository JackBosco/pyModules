from pyArgs import pyArgs
import textToArrow as tta
import addNewLine as anl
import tabifyText as tt

p = pyArgs(["in!", "out", "space"])
p.parse()
f = open(p.getArgs()["in"], 'r').read()
if 'space' in p.getArgs().keys():
    try:
        spaces = int(p.getArgs()['space'])
    except:
        raise ValueError("space arg :", p.getArgs()["space"], "must be an integer")
    if spaces > 0:
        r = tta.toArrows(tt.indentAll(anl.newLines(f), spaces))
    else:
        r = tta.toArrows(anl.newLines(f))
else:
    r = tta.toArrows(anl.newLines(f))
if "out" in p.getArgs().keys():
    open(p.getArgs()["out"], 'w').write(r)
else:
    print(r)