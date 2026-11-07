.. role:: python(code)
   :language: python

.. _code_style:

Code style
==========

In general, there are many ways in which you can format or layout your code, all of which will work. That said, how you layout your code can have a big impact on how easy it is to read and to debug.

For example, for a variable name do we use :python:`RateOfChange` or :python:`rate_of_change` or :python:`rateOfChange`? These choices don't necessarily affect what the code does, but when working as part of a team if everyone's code is formatted the same way, it makes it easier to share code and to read code written by others. 

Most  companies will have an internal style guide for how to structure and format code so that it looks consistent between different developers and is easy for different people to work on the same codebase. In large projects there may be many different people coding different parts of the program. For example, you can view the `Google style guide <https://google.github.io/styleguide/>`_. Python as a language has an official style guide known as `PEP 8 <https://peps.python.org/pep-0008/>`_. Rust also has an official `style guide <https://doc.rust-lang.org/beta/style-guide/index.html/>`_. For C and C++ there are various style guides, including the `Google C++ style guide <https://google.github.io/styleguide/cppguide.html>`_, the `Linux kernel coding style <https://www.kernel.org/doc/html/v4.10/process/coding-style.html>`_, and the `C++ core guidelines <https://isocpp.org/std/the-cpp-standard>`_.

We have our own style guide which we'll use. It's not a strict requirement, but it will help you to write code that is easier to read and debug.

.. toctree::
   :maxdepth: 1

   style_guide 

.. admonition:: This course
   
   We don't have a strictly enforced style guide. For assessed parts of the course, you'll receive marks whatever style you use.