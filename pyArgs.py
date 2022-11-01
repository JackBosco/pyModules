"""_summary_ 
    class for paring command line arguments
    created by Jack Bosco
"""
import sys

"""Parse command line arguments
args      : [name]
    if the name ends with !, the argument is not optional
self.args : {name : (value, optional)}"""
class pyArgs :
    def __init__(self, args:list()):
        self.given = sys.argv[1:]
        self.params = {}
        self.required = []
        for a in args:
            if a[-1] == '!':
                self.params[a[:-1]] = ''
                self.required.append(a[:-1])
            else:
                self.params[a] = ''
    def parse(self):
        i = 0
        while i < len(self.given) and i < 1000:
            if '=' in self.given[i]:
                s = self.given[i].split('=')
                if s[0] not in self.params.keys():
                    raise Exception("Argument invalid: " + self.given[i])
                else:
                    self.params[s[0]] = s[1]
            else:
                #parse unnamed arg in order of args left to parse
                for k in self.params.keys():
                    if self.params[k] == '':
                        self.params[k] = self.given[i]
            i+=1
        if i == 1000:
            raise Exception("Took too long to parse args")
        for r in self.required:
            if self.params[r] == '':
                raise Exception("Non-optional argument" + a[:-1] + "not given")
        