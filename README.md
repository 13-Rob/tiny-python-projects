## Book Progress
##-------------------<br>
<hr></hr>

## Notes
<p>To run a python program from the cmd you use<br></p>
<p>`$ python3 file-name`</p>

<p>To test a python script you need a test file which is going to run the actual tests.</p>
<p>The command to test files is</p>
<p>`$ pytest test file`</p>

<p>You can use the "-v" option to create a verbose output.</p>
<p>`$ pytests -v test file`</p>

<p>You can add the "-x" flag to make the tests stop on the first failing test.</p>
<p>`$ pytest -x test file`</p>

<p>You can mix the flags.</p>
<p>`$ pytest -vx test file`</p>

<p>To indicate which laguage needs to be used to execute the commands in the file. You add a special comment line that starts off with #! (called shebang).</p>
<p>This is the comment I might need.</p>
<p>`#!/usr/bin/env python3`</p>

<p>To make a program executable you use</p>
<p>`$ chmod +x program file`</p>

<p>After that you can run the program like so:</p>
<p>`$ ./program file`</p>
<p>The ./ is the current directory and is necessary.</p>

<p>The $PATH variable is a way of telling your computer to only look in places where executable programs can be found.</p>

<p>To run a program and send paramterers you can do it like so:</p>
<p>`$ ./program file parameters`</p>

<p>Most programs include arguments like "-h" and "--help", which provide help on how to use the program.</p>
<p>`$ ./program file -h parameters`</p>

<p>To add parameters we can use the argparse module.</p>

<p>A docstring is a string that occurs just after the def of a function.</p>

<p>One line conditions in python</p>
<p>`variable = value if true if condition else value if false`</p>