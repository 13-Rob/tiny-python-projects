## Book Progress
<p align=center>〜〜〜〜〜🏄🏽🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊</p>

##

## Notes
<p>To run a python program from the cmd you use</p>
<p><code>$ python3 <b>file-name</b></code></p>
<p>To test a python script with the test. The command to test a program based on a file is:</p>
<p><code>$ pytest <b>test-file</b></code></p>
<p>You can use the <b>-v</b> option to create a verbose output.</p>
<p><code>$ pytests -v <b>test-file</b></code></p>
<p>You can add the <b>-x</b> flag to make the tests stop on the first failing test.</p>
<p><code>$ pytest -x <b>test-file</b></code></p>
<p>You can mix the flags.</p>
<p><code>$ pytest -vx <b>test-file</b></code></p>

##

<p>To indicate which laguage needs to be used to execute the commands in the file. You add a special comment line that starts off with #! (called shebang).</p>
<p><code>#!/usr/bin/env python3</code></p>
<p>To make a program executable you use</p>
<p><code>$ chmod +x <b>file-name</b></code></p>
<p>After that you can run the program like so:</p>
<p><code>$ ./<b>file-name</b></code></p>
<p>The ./ is the current directory and is necessary.</p>
<p>The $PATH variable is a way of telling your computer to only look in places where executable programs can be found.</p>
<p>To run a program and send paramterers you can do it like so:</p>
<p><code>$ ./<b>file-name</b> <b>parameters</b></code></p>
<p>Most programs include arguments like "-h" and "--help", which provide help on how to use the program.</p>
<p><code>$ ./<b>file-name</b> -h <b>parameters</b></code></p>
<p>To add parameters we can use the argparse module. A docstring is a string that occurs just after the def of a function.</p>

##

<p>This is a one line condition example in python</p>
<p><code>variable = <b>value_if_true</b> if condition else <b>value_if_false</b></code></p>

## Help
<p><code>help(<b>variable</b>)</code></p>

##

### Lists
<p>Lists are mutable.</p>
<p><code>mylist = [foo, bar]</code></p>
<p>List Methods</p>
<ul>
<p>Adding elements to a list:</p>
<p><code>mylist.append('test')</code><br>
<code>$ [foo, bar, 'test']</code></p>
<p><code>mylist.extend(['test', baz])</code><br>
<code>$ [foo, bar, 'test', baz]</code></p>
</ul>

### Dictionaries
<p>Dictionary:</p>
<p><code>mydictionary = {key: value, foo: bar}</code></p>
