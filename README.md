#Progress
(##-------------------)
#Notes
To run a python program from the cmd you use
    $ python3 <program file>

To test a python script you need a <test file> which is going to run the actual tests.
The command to test files is
    $ pytest <test fiel>

You can use the "-v" option to create a verbose output.
    $ pytests -v <test file>

You can add the "-x" flag to make the tests stop on the first failing test.
    $ pytest -x <test file>

You can mix the flags.
    $ pytest -vx <test file>

To indicate which laguage needs to be used to execute the commands in the file. You add a special comment line that starts off with #! (called shebang).
This is the comment I might need.
    #!/usr/bin/env python3

To make a program executable you use
    $ chmod +x <program file>

After that you can run the program like so:
    $ ./<program file>
The ./ is the current directory and is necessary.

The $PATH variable is a way of telling your computer to only look in places where executable programs can be found.

To run a program and send paramterers you can do it like so:
    $ ./<program file> <parameters>

Most programs include arguments like "-h" and "--help", which provide help on how to use the program.
    $ ./<program file> -h <parameters>

To add parameters we can use the argparse module.

A docstring is a string that occurs just after the def of a funcction.

One line conditions in python
    <variable> = <value if true> if <condition> else <vale if false>