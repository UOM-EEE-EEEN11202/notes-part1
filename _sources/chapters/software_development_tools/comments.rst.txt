.. role:: python(code)
   :language: python

.. role:: rust(code)
   :language: rust


Comments
========

Comments allow you to add non-executable information into your code. The are intended for the developer (you or another team member working on making, supporting or updating the code). Generally they are used for explaining what the code is doing and why, to keep track of what this unit of code is for, and to explain anything which might not be obvious. Sometimes they are used to deactivate code that you have written, but don't want to be part of the program at the moment for whatever reason.

Typically comments represent `about 20% of the lines of code that are actually written <https://ieeexplore.ieee.org/abstract/document/5070980>`_. The form a substantial part of any program. Comments aren't a substitute for good documentation though. They can usually only be text (no diagrams or similar) and they sit at a particular place in your code and so generally explain what's happening only there, rather than giving the big picture. Nevertheless, comments are an essential part of any code.

In Python, lines that start with a hash :python:`#` are comments. In Rust, lines that start with two forward slashes :rust:`//` are comments. Comments can start at any point during a line of code. 

Examples of Rust comments might be:

.. code-block:: rust

    // This is a comment at the start of the file.
    // We usually include some lines at the top of a file
    // to explain what the code is for, what it's trying to do.
    // This usually includes who wrote it, a license
    // a copyright statement, and so on.
    
    fn main() {
        let i = 0;  // comment in-line with code. 
                    // This code is run, the
                    // comment helps explain what it does 

        // let i = 1; // this code is commented out 
                      // It won't run
    }

.. admonition:: This course

   We'll expect you to use suitable comments to document and explain your code. You might lose marks in the lab tasks and/or in the exam if you don't have any comments present.