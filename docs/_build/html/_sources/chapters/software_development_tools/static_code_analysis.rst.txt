.. role:: rust(code)
   :language: rust

Static code analysis
====================

Static code analysis refers to checking your code for errors, before you run or compile the code. This can avoid you wasting time trying to run code which has known issues or other reasons why it might not work. Remember, our simple examples will likely run or compile in a few seconds, but real programs with thousands or millions of lines of code might take hours or more to compile, and so failed compilations can be a real time drain.

There are many different types of static code analysis. 

*Linting* is essentially a spell-check of your code. The example below shows Rust program code. It has detected that the variable :rust:`j` (and indeed :rust:`i` in this simple example) is never used. It's checking that this is what you want, because it might indicate a mistake, and suggested using the preferred (but optional) of using :rust:`_j` to indicate it's deliberately not used for some reason. Indeed for a simple error like this offers a *Quick Fix* to automatically correct it for you. 

.. figure:: linting.png
  :width: 800
  :align: center
  :alt: Example of static code analysis in VSCode

Linting is probably the most common form of static code analysis that you'll encounter. If desired, there are many other checks you can perform via static code analysis. For example, you can get analyzers that compare your code against a given style guide, or analyzers that examine the code for known security risks. We would encourage you to explore the VSCode interface, documentation, and online help to explore what other types of analysis might be useful.

.. admonition:: This course

   We've set up the development tools to do linting automatically. We won't cover other forms of static code analysis. 