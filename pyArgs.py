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
        self.args = args
        self.given = sys.argv[1:]
        for a in self.args:
            if a[-1] == '!' and a not in self.given:
                raise Exception("Non-optional argument" + a[:-1] + "not given")
        self.params = {}
    def parse(self):
        timeout = 0
        while len(self.given) > 0 and timeout < 1000:
            if self.given[0][0] == '/':
                self.params[self.given[0][1:]] = self.given[1]
                self.given = self.given[2:]
                
            else:
                raise Exception("Argument invalid: " + self.given[0])
            timeout +=1
        if timeout == 1000:
            raise Exception("Took too long to parse args")
        