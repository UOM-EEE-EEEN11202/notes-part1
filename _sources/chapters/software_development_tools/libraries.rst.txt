.. role:: console(code)
   :language: console

.. role:: python(code)
   :language: python

.. role:: rust(code)
   :language: rust

.. _libraries:

Modules, libraries, and similar
===============================

You don't necessarily have to write all of your code yourself! There is lots of code that has already been written. Lots of it is freely available on the Internet for others to use, for example on sites like `GitHub <https://github.com/>`_.

There's also code, generally known as *modules* or *libraries* or *packages* which extend what the base programming language can do. Using these is very common. (We'll generally use the terms modules, libraries, and packages inter-changeably, even if technically they'll all slightly different things.)

There are three broad categories of external code that you might add in to your code.


.. _standard_library:

Standard library
----------------
Most programming languages only have a very limited number of commands enabled by default. This helps keep the resulting programs small and limits the potential attack vector for security bugs and similar. 

The *standard library* is installed automatically, whenever you set up your programming tools/environment, and so it always available for your code to use. To use functions in the standard library you need need to add :python:`import` or :rust:`use`, or similar, the parts that you want. That is, you have to explicitly say which parts you want to use.

For example, in Python you might add

.. code-block:: python

   import math

to add maths functions to the code. In Rust you might add

.. code-block:: python

   use std::io;

to add functions for reading input from the command line, and displaying output back to the terminal. 

There are lots of functions available in the standard library. We won't cover them all here, but you will encounter lots as you move through the course.


Packages from online repositories
---------------------------------
There are many libraries available on the Internet to extend the functionality of the base programming language. These are stored in *repositories*. 

For Python, `PyPi <https://pypi.org/>`_ is a common repository for packages. Indeed it is likely the default one used unless you change your Python configuration. At the command line there is a Python tool called :console:`pip` which you can use to install additional modules from the Internet. You add these to your code with an :python:`import` command. We'll see examples of doing this in the labs. 

For Rust, `crates.io <https://crates.io/>`_ will be the default repository for packages. In Rust, you list :rust:`[dependencies]` in the :console:`Cargo.toml` project configuration file and add these to your code with the :rust:`use` command. Again, we'll see examples of doing this in the labs. 

For C/C++, `vcpkg <https://vcpkg.io/en/>`_ is commonly used. 


Code from online sites such as GitHub
-------------------------------------
The packages above have been *pre-packaged*. You download them and add them to your code, without necessarily ever seeing the actual code that you're downloading. There are tools, such as :console:`pip` to make working with packages easier. 

In contrast, sites such as `GitHub <https://github.com/>`_ share raw source code. How to interact with this is up to you. You may copy-and-paste just some small sections of the code which are relevant to what you want; or you may download the whole project and add it to your own. Using code from a source like `GitHub <https://github.com/>`_ is useful if you want/need to be able to see how the code works, rather than just using the functionality a package provides in an *opaque box* manner.


.. _code_security:

Important considerations
------------------------

.. danger::

    When downloading code from others/the Internet, make sure you think about cybersecurity before doing so. If you let code run on your computer, it may have access to your files, to leak information to others, or to take various other malicious actions.

    In general, we would trust items in the standard library without too much further consideration. For external packages, there are very commonly used ones, such as numpy and matplotlib, and again we would likely trust these without too much further consideration. For more obscure packages, it may be that more thought is warranted. 

    Most companies will probably restrict which external packages you can install to a pre-defined set which have been through some form of a security audit. 


.. caution::

   Just because code or pre-defined packages are openly available on the Internet doesn't necessarily mean that they give you the correct permissions to use them in your project. We will discuss :ref:`software licenses <software_licenses>` in more detail later. Briefly, code usually comes with a set of terms and conditions giving constraints on how it can be used. Potentially, these terms could be incompatible with the needs of your project, and may limit what can be used. 

   Before using external code, make sure you check how it is licensed and what constraints or obligations the license places on the user.

   All also of course need to check that any external code actually works! It's possible it contains bugs and won't work perfectly when you try to use it.


.. admonition:: This course

   We'll use external packages a lot throughout the course, and having knowledge of some common packages (e.g. Numpy, Scipy, Pandas/Polars, Matplotlib) is a topic we'll cover. 

   In the development environment we've not added any constraints on what packages can be installed, so that you can explore. Be aware that you might not have access to any arbitrary package in the exam or in your more general programming practice however. 

