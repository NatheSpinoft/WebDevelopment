# First few lessons

## Topic: Clang++ compiler
I have learned that the clang++ is the compiler from the xcode that is installed in the make OS to compile the code so that the filename.cpp is presented without a file without a file extension

### How would i teach it to someone new
The command is 
>clang++ filename.cpp -o filename

### What remains to be understand 
What the -o represents. It falls under Code generation options.

## Topic: First line of code of C++ 
The hashtag(#) is the first letter introduced along with "include" which introduces the library involved. The library is the second snippet of code on the same line enclosed with "<>". in the most recent of cases its iostream / input output stream.

### How would i teach it to someone new
It is "#include <iostream>"

### What remains to be understood 
iostream can be suffixed starting with a period so that elemnts can be introduced.

## Topic: Second Line of code
The code "using namespace std" basically means that if there is a standard input output function already in the library using the iostream we should use the one in session

### how would i teach it to someone new
The code
>using namespace std

### What remains to be understood
is it similar to python's import function?

## Topic: Next line > int main(void)
Int states that this specific function will send back an integer to the computer
main states that this is a function to the main output
(void) states that there are no parameters to the main output

### How would i teach it to someone
the command is
>Int main(void)

### What remains to be understood
Are there more variations of this

## Topic: Next line >cout << "Hello World";
Cout is used to display output
<< is used next to cout to print or display the next items for output with quotes

### How would i teach it to someone
the codes is 
>int main() {

>cout << "Hello world";    

>return 0;

>}

### What remains to be understood
Are there different versions of cout

## Topic: Next line > return 0;
return 0; ends the program

### How would i teach it to someone
it wraps within the {}

> return 0;

>}

### What remains to be understood
can a return value be used as a funciton