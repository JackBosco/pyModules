# pyModules
Misc. Modules I made in python
***Author: Jack Bosco***

## pyArgs.py
Class for parsing command line arguments  
Arguments can be in the following syntax:  
`python program_name.py x=5 text=hello` *unordered*  
`python program_name.py 5 hello` *ordered*

Required arguments:
- specified with `!` at the end of the argument name
- omit the `!` when specifying the argument in the command line

Raises:
- Exception: `Argument invalid: *arg` arg (to the left of the =) is not in the specifications
- Exception: `Took too long to parse args` (>= 1024 attempts to parse args)
- Exception: `Missing required argument: *arg` arg is specified as required, but it was not found in the command line arguments given

Returns:
- pyArgs: a parser for command line arguments, with a dictionary self.args mapping the variables in the specifications to values from the command line

## addNewLine.py
Copy and paste functionality for LaTex newlines.  
Copy the plain text. Paste into a text file. On runtime, specify input(required) and output files in the command line **including extensions**.  

> args: in!, out  

*If no output file is specified, output printed to the command line*

## tabifyText.py
Copy and paste functionality for LaTex to indent every line by "space" spaces usine `\hspace{}`.

1. Copy the plain text. Paste into a text file. 
2. On runtime, specify input(required) and output files **including extensions** as well as the number of spaces to indent in the command line.

> args: in!, space!, out

*If no output file is specified, output printed to the command line.*

## textToArrow.py
Copy and paste functionality for LaTex arrows.

1. Copy the plain text arrow characters 
2. Paste into a text file. 
3. On runtime, specify input(required) and output files in the command line **including extensions**

> args: in!, out

*If no output file is specified, output printed to the command line.*

Arrows are: 
- These three specific unicode characters in order:
    > chr(226) chr(8224) chr(8217)
- OR this one unicode character:
    > chr(8594)
- OR these two characters in order:
    > ->
- OR these three characters in order:
    > -->
