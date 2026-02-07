.. role:: python(code)
   :language: python

Formatters
==========

We mentioned `style guides previously <https://uom-eee-eeen11202.github.io/chapters/useful_information/style_guide.html>`_. There are lots of choices for how we layout code. For example, do we use AAAA or aaaa as a variable name? These choices don't necessarily affect what the code does, but when working as part of a team if everyone's code is formatted the same way, it makes it easier to share code and to read code written by others. 

To help with this, there are automatic formatting tools, such as `Ruff <https://docs.astral.sh/ruff/>`_ for Python, and `rustfmt <https://github.com/rust-lang/rustfmt>`_  for Rust. These will re-layout your code automatically to try and keep it correctly on a specified style. 

For example, in Python it might convert single quotes :python:`''` into double quotes :python:`""`. In many places in Python, both styles of quote work in exactly the same way, but a style guide will say that one of the ways is preferred. (Probably double quotes.)

.. admonition:: This course

    You don't need to learn anything about formatters. In the EEEN11202 devcontainer, we have turned on *format on save* automatically for Python and Rust files. This means that each time you save your code file the auto-formatter will automatically be applied to your work. It may change some of your code to put it onto the correct style. 