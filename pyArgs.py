"""
Author: Jack Bosco (2022)
"""
import sys
class pyArgs :
    """class for paring command line arguments
        arguments can be in the following syntax:
            python program_name.py x=5 text=hello
            python program_name.py 5 hello 

    Raises:
        Exception: \"Argument invalid: arg\" arg (to the left of the =) is not in the specifications
        Exception: \"Took too long to parse args\" (>= 1000 attempts to parse args)
        Exception: \"Missing required argument: arg\" arg is specified as required, but it was not found in the command line arguments given

    Returns:
        pyArgs: a parser for command line arguments, with a dictionary self.args mapping the variables in the specifications to values from the command line
    """
    def __init__(self, specifications:list()):
        """Initializer
        Args:
            specifications (list): specify the variable names to be parsed for in the command line, these will be the keys of self.args. \
            Append \'!\' to indicate a required argument, the \'!\' is stripped from the specifications and will NOT be included in the variable name. DO NOT include the \
                \'!\' when accessing values from self.args or specifying args in the command line (to the left of the =).
        """
        self._given = sys.argv[1:]
        self._literal = []
        self.args = {}
        self._required = []
        for a in specifications:
            if a[-1] == '!':
                self._required.append(a[:-1])
            self._literal.append(a.strip('!'))
    def parse(self):
        """Parses command line

        Raises:
        Exception: \"Argument invalid: arg\" arg (to the left of the =) is not in the specifications
        Exception: \"Took too long to parse args\" (>= 1000 attempts to parse args)
        Exception: \"Missing required argument: arg\" arg is specified as required, but it was not found in the command line arguments given
        """
        i = 0
        while i < len(self._given) and i < 1000:
            if '=' in self._given[i]:
                s = self._given[i].split('=')
                if s[0] not in self._literal:
                    raise Exception("Argument invalid: " + self._given[i])
                else:
                    self.args[s[0]] = s[1]
            else:
                #parse unnamed arg in order of args left to parse
                for l in self._literal:
                    if l not in self.args.keys():
                        self.args[l] = self._given[i]
                        break
            i+=1
        if i == 1000:
            raise Exception("Took too long to parse args")
        for r in self._required:
            if r not in self.args.keys():
                raise Exception("Missing required argument: " + r)
    def getArgs(self) -> dict:
        """getter method for arguments parsed. This will be empty before running parse().
        
        Returns:
            dict: self.args maps the variables in the specifications to values parsed from the command line
        """
        return self.args