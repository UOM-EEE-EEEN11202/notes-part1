.. role:: console(code)
   :language: console

Scripts vs. programs
====================
Firstly, a small topic for completeness. 

In early parts of the course we will speak mainly about *scripts*. In the latter parts we will speak mainly about *programs*. 

We mentioned interpreted and compiled languages previously :ref:`previously <language_types>`. A script means it's interpreted code. That is, it runs line by line directly from the code file. 

A program means it's compiled code. Before we can run the code, our source code (e.g. a :console:`.rs` file) is first converted from a human readable format into something the computer can execute. This makes a new file, often (but not always) with a :console:`.exe` extension. It is this *executable* that the computer actually runs. If the compilation step fails, no executable will be produced and there won't be anything for the computer to run. 

This probably makes small practical difference when you're first starting out. We wanted to mention it here to make sure you don't get confused if you see *script* rather than *program*. 