.. _documentation_tools:

Documentation tools
===================
Generally comments are quite low level, giving details on exactly what that piece of code is aiming to do and any hints needed to understand how it works and complicated operations. Docstrings sit at a level above this, giving details on how to use the code. 

In contrast, documentation is a level higher still, explaining the overall architecture and design choices made. 

You can just write documentation in a word processor such as Microsoft Word or Google Docs and store the file(s) together with the source code for your program. Alternatively, there are lots of dedicated tools available to help you write and maintain documentation. These tools can also help display docstrings in a more user friendly manner, so the user isn't looking at the source code for the program. 

As one example, `Sphinx <https://www.sphinx-doc.org/en/master/>`_ takes documentation written as text and converts it to be an interactive website which can include code examples and other features. It is used in website such as `Read the Docs <https://about.readthedocs.com/>`_ which is commonly used to share documentation for open source programs. Alternatively, `DOxygen <https://www.doxygen.nl/>`_ takes the code file, including comments and docstrings, and helps convert them to be a website, which can include text and code, and have hyperlinks to move between different functions.

The different tools available each have their own syntax and detailed methods of using them.

.. |ico1| image:: GitHub_Invertocat_Dark.svg 
            :width: 20

.. admonition:: This course

   For this course, we don't expect you to use, or have any specific knowledge on these types of documentation tools. 
   
   If interested, for these notes, Parts 0, 1 and 2 are written using `Sphinx <https://www.sphinx-doc.org/en/master/>`_. These are the more Python parts of the notes, and so the documentation is using Sphinx as a tool written in Python. Part 3, focusing more on Rust, is written using `mdBook <https://rust-lang.github.io/mdBook/>`_, a documentation tool written in Rust. 
   
   For all parts of the notes you can click on the GitHub (|ico1|) icon at the top of the page if you want to see the source code for how we've made use of these tools. 