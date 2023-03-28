To run a python program from the cmd you use
    $ python3 <file to run>

To test a python script you need a <test file> which is going to run the actual tests.
The command to test files is
    $ pytest <test fiel>

You can use the "-v" option to create a verbose output.
    $ pytests -v <test file>

You can add the "-x" flag to make the tests stop on the first failing test.
    $ pytest -x <test file>

You can mix the flags.
    $ pytest -vx <test file>

