print("""
     'and' -  is a logical operator to combine two conditions, it returns true if both are true
     'del' - deletes objects, variables, lists or attributes
     'from' - is part of the import features and includes subs
     'not' - negates a the truth value or expression
     'while' - a continuos loop until a condition is met
     'as' - part of the import feature that turns a module into an alias, can also alias a function      
     'elif' - part of the if statements as if one condition is not true the elif is then implemented
     'global' declares a variable to be global
     'or' - is a logical operator to combine conditions, either/or would be true if one condition is true
     'with' - wraps execution of code using entering and exiting the module
     'assert' - tests a condition and raises assertion error following the comma when it fails
     'else' - when if cases have been gone through else is implemented following the next code block within
     'if' - situationally assess cases by conditions
     'pass' - a placeholder for code to be implemented later
     'yield' - a resource management implementation that generates values on the fly remaining the same resources
     'break' - terminates a loop and passes over to the next code
     'except' - error handling that is passed and goes to the next code
     'import' - a way to import modules
     'print' - prints on screen
     'class' - blueprint for creating objects
     'exec' - allows for dynamic executions
     'in' - is used to check memberships in tuples, sets, and strings and returns true.
     'raise' -  allows you to raise exceptions and print a statement
     'continue' - allows the skip over an iteration
     'finally' - part of the try and except block, is used as final exeuction
     'is' -  compares conditions and returns if both are from the same memory block
     'return' - used in a fuction to return the execution of codes in the block
     'def' - used to create functions
     'for' - used to create loops
     'lambda' - used to create short and simple functions
     'try' - used to go through codes that can go through exceptions
      
    Escape sequences in Python

    \\ - Backslash: Represents a single backslash character.
    backslash = "This is a backslash: \\"

    \' - Single Quote: Represents a single quote character inside a string.
    single_quote = 'It\'s a sunny day!'

    \" - Double Quote: Represents a double quote character inside a string.
    double_quote = "She said, \"Hello!\""

    \a - Bell: Triggers the system bell (if supported by the environment).
    bell = "\a"  # May produce a sound

    \b - Backspace: Moves the cursor back one space (erases the previous character).
    backspace = "Hello\b World!"  # Produces "Hell World!"

    \f - Form Feed: Moves the cursor to the next page (rarely used in modern applications).
    form_feed = "Hello\fWorld!"  # Moves to the next page

    \n - New Line: Moves the cursor to the next line.
    new_line = "Hello\nWorld!"  # Produces:
    Hello
    World!

    \r - Carriage Return: Moves the cursor to the beginning of the current line.
    carriage_return = "Hello\rWorld!"  # Produces "World!" (overwrites "Hello")
    
    \t - Horizontal Tab: Inserts a horizontal tab space.
    tab = "Hello\tWorld!"  # Produces "Hello    World!" (with a tab space)

    \v - Vertical Tab: Moves the cursor down to the next vertical tab stop (less commonly used).
    vertical_tab = "Hello\vWorld!"  # Moves down vertically

    Format specifiers in Python

    %d - Signed Decimal Integer: Formats an integer in decimal notation.
    decimal = "Integer: %d" % 42  # Output: "Integer: 42"

    %i - Signed Decimal Integer: Same as %d, used for integer representation.
    integer = "Integer: %i" % -7  # Output: "Integer: -7"

    %o - Octal Integer: Formats an integer in octal (base 8) notation.
    octal = "Octal: %o" % 8  # Output: "Octal: 10"

    %u - Unsigned Decimal Integer: (Deprecated in Python 3) Used to format a non-negative integer.
    unsigned = "Unsigned: %u" % 42  # Output: "Unsigned: 42"

    %x - Hexadecimal Integer (lowercase): Formats an integer in hexadecimal (base 16) using lowercase letters.
    hex_lower = "Hex (lowercase): %x" % 255  # Output: "Hex (lowercase): ff"

    %X - Hexadecimal Integer (uppercase): Formats an integer in hexadecimal using uppercase letters.
    hex_upper = "Hex (uppercase): %X" % 255  # Output: "Hex (uppercase): FF"

    %e - Scientific Notation (lowercase): Formats a floating-point number in scientific notation.
    scientific_lower = "Scientific (lowercase): %e" % 12345.67  # Output: "Scientific (lowercase): 1.234567e+04"

    %c - Character: Formats an integer as a character.
    character = "Character: %c" % 65  # Output: "Character: A"

    %r - Representation: Formats using the `repr()` function, showing the string representation of an object.
    representation = "Representation: %r" % "Hello"  # Output: "Representation: 'Hello'"

    %s - String: Formats a string (uses `str()` by default).
    string = "String: %s" % "Python"  # Output: "String: Python"

    %% - Percent Sign: Outputs a literal percent sign.
    percent_sign = "This is 100%% correct."  # Output: "This is 100% correct."

    %E - Scientific Notation (uppercase): Same as %e but uses uppercase "E".
    scientific_upper = "Scientific (uppercase): %E" % 12345.67  # Output: "Scientific (uppercase): 1.234567E+04"

    %f - Floating Point: Formats a floating-point number.
    floating_point = "Floating Point: %f" % 3.14159  # Output: "Floating Point: 3.141590"

    %F - Floating Point (same as %f): Equivalent to %f, used for floating-point representation.
    floating_point_f = "Floating Point (F): %F" % 3.14159  # Output: "Floating Point (F): 3.141590"

    %g - General Format: Formats a floating-point number using either %f or %e, whichever is shorter.
    general = "General: %g" % 0.000123456  # Output: "General: 0.000123456"

    %G - General Format (uppercase): Similar to %g but uses uppercase for scientific notation.
    general_upper = "General (uppercase): %G" % 123456.0  # Output: "General (uppercase): 1.23456E+05"

    {} - is used as a format for displaying python's print f features, also used to create dictionaries. in python 3.8 
    they are mutable
      """)