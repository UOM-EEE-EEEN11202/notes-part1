.. role:: python(code)
   :language: python

.. role:: rust(code)
   :language: rust

.. _scope:

Scope and namespaces
====================

Our programs will contain a range of data and functions. Best practice is that these have a defined *scope* for where they can be seen and used. That is, a function can only use data that it in its scope - data that it's been given access to. 

We don't want all of our data and functions to be available everywhere: it's bad practice from a security point of view, and can lead to data accidentally being changed. Say you have a variable :python:`x1` in one part of the code, and :python:`x2` in another part of the code. If these were available everywhere, a single typo, having a :python:`2` instead of a :python:`1` would mean your function was working with the wrong data. Moreover, it's common that we want to use the same (or same-ish) names for things in multiple places. Having a local scope lets us do this, re-using variable names without different functions or parts of the program interfering with each other.

Scope
-----
In most programming languages a scope block is defined by curly brackets :rust:`{}`. In Python it's defined by indented white space (usually 4 spaces). To give a Python example, the below has two functions:

.. code-block:: python

   def my_add(a,b):
       c = a + b
       return c

   def my_substract(a,b):
       c = a - b
       return c

Both of these use the same variable names internally, and that's completely fine because the variables are *local* to each function. When the function finishes running, the variables go *out of scope* and are no longer accessible.

So, say you had the code

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

   x = "Hello"
   def my_func():
       x = "world"
   my_func()
   print(x)

What is the value of :python:`x` on line 5? It is :python:`"Hello"`. The function :python:`my_func()` runs on line 4, and sets :python:`x = "world"`. However, when the function finshes, and the code moves on to line 5, this defintion of :python:`x` goes out of scope, and the earlier definition of :python:`x = "Hello"` comes back in to scope. 

There is also a *global* scope, which everything in the program can see. In general however, for a function to be able to see and interact with data, the data should be provided as an input to the function (possibly via a :ref:`pointer <pointers>`). Any changed data should be provided as an output (again possibly using :ref:`pointers <pointers>`). 


Namespaces
----------
*Namespaces* help us to re-use function names in different parts of a program. Apart from a few core parts of a programming language, and functions we've made ourselves in the same code file, functions have to explicitly be brought into scope in order for our program to be able to see and use them.

In Python this is done with :python:`import`. Rust has :rust:`use`. For example, in Python it's common to have code such as

.. code-block:: python

   import numpy as np

This brings the :ref:`library <libraries>` :python:`numpy` into scope, and gives it the shorter name :python:`np`. Numpy is commonly used in engineering tasks and we'll see it in the lab. It provides a function sum. We access this as :python:`np.sum()` rather than just :python:`sum()`. :python:`sum()` is a valid Python command, but is different to :python:`np.sum()`. Having the namespace :python:`np.` helps make it explicit which function we want to use. You can think of the namespace as giving an *address* of which function to use.

In languages other than Python it's common to use two colons :rust:`::` to separate steps in the namespace. For example, you might have code such as

.. code-block:: rust

   use std::io;

This bring a wide number of input/output functions, which are part of the :ref:`standard library <standard_library>`, into scope.