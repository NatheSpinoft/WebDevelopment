# Import
The import function is used to import sys and at times it can be used as the third argument if using
>from sys import argv
to import from a library 

# The function

## The first line
the function is first presented by
>def conversion (Celsius):

which the def defines the name of the function which comes second and following the () parameters. Must close the line with a colon :

## The body
the body usually contains content

## The last line
the last line is the return which returns the results

# The name and main portion for argv

## if __name__ == "__main":
the portion of if __name__ comes first then double equal signs followed by quotes on __main___. Remember that name comes first then main and main is quoted followed by a colon

## if len(sys.argv) !=2:
There is a second if statement nested in the name if funciton which uses from the system library argv portion which if the script ran without 2 args it would display a print screen.

## the last line of the block 
sys.exit(1) a system exit 

## Try block
the try has a colon and what follows is the float for the system argv value with the argument followed by the script
>try:

>celsius = float(sys.argv[1])

The following command, 

>except ValueError:

indicates except for value errors print a statement for informing the user to enter a value. 

Then close with sys.exit(1)





