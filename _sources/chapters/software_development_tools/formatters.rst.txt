.. role:: python(code)
   :language: python

.. role:: console(code)
   :language: console

Formatters
==========

We mentioned `style guides previously <code_style>`_. There are also automatic tools that you can use to check your code style against a standard, and to automatically convert code between different styles. Tools, such as `Ruff <https://docs.astral.sh/ruff/>`_ for Python, and `clang-format <https://clang.llvm.org/docs/ClangFormat.html>`_ for C/C++ will re-layout your code automatically to try and keep it correctly on a specified style. 

For example, in Python it might convert single quotes :python:`''` into double quotes :python:`""`. In many places in Python, both styles of quote work in exactly the same way, but a style guide will say that one of the ways is preferred. (Probably double quotes.)

.. admonition:: This course

    You don't need to learn anything about formatters other than to know that they exist. 
    
    In the EEEN11202 :ref:`devcontainer <environment_control>`, we have turned on *format on save* automatically for your files. This means that each time you save your code file the auto-formatter will automatically be applied to your work. It may change some of your code to put it onto the correct style. For example, in the files we have pre-configured for the labs, you will see there is a :console:`.clang-format` `file <https://github.com/UOM-EEE-EEEN11202/vscode-setup/blob/main/.clang-format>`_  which defines the style to be used for C/C++ code.