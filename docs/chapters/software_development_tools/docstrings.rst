.. role:: python(code)
   :language: python

.. role:: rust(code)
   :language: rust

Docstrings and doctests
=======================

Comments sit alongside code and are intended for the developer(s) of the code. They usually help explain how the code works, any non-obvious steps, and so on. 

In addition to comments, many programming languages support *docstrings*. These are inside the code file, but are intended for the user. They may contain instructions on how to use the code, examples of the different options that are possible, and so on. They thus complement comments, being aimed for a different audience. Rather than the user opening the code file, there is often :ref:`another tool <documentation_tools>` that displays docstrings to the user via a nicer interface.

In Python these are blocks of text inside three apostrophes :python:`'''`, for example

.. code-block:: python

	''' This is documentation.
	Text and code in this block will be included in documentation.'''
	...
	# This is a comment. It won't be included in automatically generated documentation. 
    
In Rust the equivalent uses three forward slashes :python:`///`

.. code-block:: rust

	/// This is documentation.
	/// Text and code in this block will be included in documentation.
	...
	// This is a comment. It won't be included in automatically generated documentation. 

In this type of documentation for the user of a piece of code, it's often useful to give some examples, showing how to use the functions. Of course it's important that these examples are correct! *doctests* are a type of :ref:`unit testing <unit_testing>` where the code given inside a docstring is tested to see whether it works (as opposed to testing the code in the main file). 

In Rust, blocks of code which are inside three apostrophes :rust:`'''`, and also inside a docstring, can be tested using doctest tools. An example in Rust code might be

.. code-block:: rust

    /// This is documentation.
    /// Text and code in this block will be included in documentation.
    /// ```
    /// let i = 0;
    /// i = i + 2;
    /// ```

.. admonition:: This course

   We will have a handful of examples using docstrings and doctests. We expect you to know that they exist, and to have a passing familiarity, but not to have a lot of depth of knowledge. 