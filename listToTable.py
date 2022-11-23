"""
Returns tabular in LaTex syntax from a python printed list
WORK IN PROGRESS
"""
def run(rows:list, null="NULL"):
    ret = ""
    nCols = 1
    for r in rows:
        if type(r) == list and len(r) > nCols:
            nCols = len(r)
    ret += "\\begin{tabular}{|" + "c|" * nCols + "}\n"
    for r in rows:
        ret += "\t\\hline\n\t"
        colsFilled = 0
        if type(r) == list:
            for c in r:
                ret += str(c) + " & "
                colsFilled += 1
        else:
            ret += str(r)
            colsFilled += 1
        while colsFilled < nCols:
            ret += null + " & "
            colsFilled += 1
        ret = ret[:-3] + "\\\\\n"
    return ret + "\t\\hline\n\\end{tabular}"


def main():
    from pyArgs import pyArgs
    p = pyArgs(["out"])
    p.parse()
    l = [[1,2,3],[4,5,6, "lonely cell"],[7,8,9]]
    r = run(l)
    if "out" in p.getArgs().keys():
        open(p.getArgs()["out"], 'w').write(r)
    else:
        print(r)

if __name__ == '__main__':
    main()