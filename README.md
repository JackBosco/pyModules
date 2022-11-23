# pyModules
Various Modules I made to copy and paste plain text into LaTex code
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

## combine.py
Supports chaining together up to three pyModule transformations on a given input in a sweet looking one-liner. Transformation output is fed into the next trasformation in sequential order, i.e. `input -> first! -> second -> third -> output`
> args:
> - in! :  input file with extension (required)
> - first! : first transformation on input (required) (options are textToArrow : t2a, addNewLine : aNL, tabifyText: tab)
> - second : second transformation on input (options are textToArrow : t2a, addNewLine : aNL, tabifyText : tab)
> - third  : third transformation on input (options are textToArrow : t2a, addNewLine : aNL, tabifyText : tab)
> - spaces : `int`, optionally specify the amount of spaces to tabify if tab is included. Default is 4.
> - out : output file. Defaults to command line if not specified
>> Examples:  
>> `% python3 ~/Documents/pyModules/combine.py in=temp.txt first=aNL second=t2a third=tab spaces=1`  
>> `% python3 ~/Documents/pyModules/combine.py in=temp.txt aNL tab out=newFile.txt`

***if you read this far, THANK YOU***
