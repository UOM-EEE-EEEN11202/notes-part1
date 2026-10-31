.. role:: python(code)
   :language: python

Code style and auto-formatters
==============================

Code style
----------
In general, there are many ways in which you can format or layout your code, all of which will work. That said, how you layout your code can have a big impact on how easy it is to read and to debug.

For example, do we use :python:`RateOfChange` or :python:`rate_of_change` or :python:`rateOfChange` as a variable name? These choices don't necessarily affect what the code does, but when working as part of a team if everyone's code is formatted the same way, it makes it easier to share code and to read code written by others. 

Most  companies will have an internal style guide for how to structure and format code so that it looks consistent between different developers and is easy for different people to work on the same codebase. In large projects there may be many different people coding different parts of the program. For example, you can view the `Google style guide <https://google.github.io/styleguide/>`_. Python as a language has an official style guide known as `PEP 8 <https://peps.python.org/pep-0008/>`_. Rust also has an official `style guide <https://doc.rust-lang.org/beta/style-guide/index.html/>`_. For C and C++ there are various style guides, including the `Google C++ style guide <https://google.github.io/styleguide/cppguide.html>`_ and the `Linux kernel coding style <https://www.kernel.org/doc/html/v4.10/process/coding-style.html>`_.

We have our own style guide which we'll use. It's not a strict requirement, but it will help you to write code that is easier to read and debug.

.. toctree::
   :maxdepth: 1

   style_guide 



Auto-formatters
---------------
There are also automatic tools that you can use to check your code style against a standard, and to automatically convert code between different styles. In our setup of VSCode we automatically turn these on to help with formatting your code. You'll find that your code gets re-formatted by the auto-formatter each time you save it. Beyond this, we don't have a strictly enforced style guide. For assessed parts of the course, you'll receive marks whatever style you use.  


To help with this, there are automatic formatting tools, such as `Ruff <https://docs.astral.sh/ruff/>`_ for Python, and `clang-format <https://clang.llvm.org/docs/ClangFormat.html>`_  for C/C++. These will re-layout your code automatically to try and keep it correctly on a specified style. 

For example, in Python it might convert single quotes :python:`''` into double quotes :python:`""`. In many places in Python, both styles of quote work in exactly the same way, but a style guide will say that one of the ways is preferred. (Probably double quotes.)

.. admonition:: This course

    You don't need to learn anything about formatters. In the EEEN11202 devcontainer, we have turned on *format on save* automatically for your files. This means that each time you save your code file the auto-formatter will automatically be applied to your work. It may change some of your code to put it onto the correct style. 