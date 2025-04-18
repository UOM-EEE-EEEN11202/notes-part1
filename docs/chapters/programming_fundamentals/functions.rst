
.. role:: python(code)
   :language: python

.. _functions:

Functions
=========

Fundaments 
----------

Functions are the basic building blocks of a code file. They are re-usable blocks of code that perform a clear specified operation. When getting started, the art of programming is knowing which built-in functions are available for you to use, how to combine these together, and how to write your own functions when the operation you need isn't already available to use.

A simple function in Python might be

.. code-block:: python 

    def add_and_multiply(a, b):
        c = 3 * (a + b)
        return c

:python:`add_and_multiply` is the name of the function. This can be whatever is meaningful to us to describe, briefly, what the function does. This particular function takes two inputs, called :python:`a` and :python:`b`, with these defined by the round brackets :python:`()` after the function name. The function has one output (it could have more if we wanted). The output is called :python:`c`, and the keyword :python:`return` flags this as being the output. There's just one line of code that does the hard work in this example, :python:`c = 3 * (a + b)`. We could have lots and lots of lines here though if they were needed. 

In another function, we can then *call* this function, and it will *return* its output. For example we might have

.. code-block:: python 

    def main():
        a = 3
        b = 1
        c = add_and_multiply(a, b)

If just using :python:`add_and_multiply` once this isn't necessarily that helpful, but the aim is that the :python:`add_and_multiply` function is reusable. We can have code such as 

.. code-block:: python 

    def main():
        a = 3
        b = 1
        c = add_and_multiply(a, b)
        b = 6.43
        c = add_and_multiply(a, b)
        d = 22
        e = -1
        f = add_and_multiply(d, e)

and use the function lots of times. This way, when testing the code, we can run :ref:`unit tests <unit_testing>` on :python:`add_and_multiply`, and when we're confident it's working it gives us more confidence :python:`main` will be working as we want. 

Note that in the last call to :python:`add_and_multiply` in :python:`main` above, we gave the inputs and outputs different names. This is completely valid and very helpful, they're still called :python:`a`, :python:`b`, and :python:`c` inside the :python:`add_and_multiply`, but in the calling function :python:`main` we can use different names, whatever is more meaningful for that piece of code. 


The main function
-----------------

By convention, when a program first starts it runs the function called *main*. Many programs expect a function called main to be present in any code at some point. Main gives the *entrypoint* and means that as a programmer we always know what will run first, and we can then branch off into other functions as needed from there.

For Python, but not other languages, a bit of additional code is actually needed to get it to start off by running main. This looks like

.. code-block:: python
    
    def main():
        print("Hello world")


    if __name__ == "__main__":
        main()

The :python:`if __name__ == "__main__":` is just part of the *boilerplate* code that we need to make things work. This example is specific to Python. It's not needed in other programming languages, they will pick up the main function automatically. Although, other languages may well need their own boilerplate code in different places to make things work. 

In general, best practice is to put as little as possible into the :python:`main` function. It's better to do whatever setup is needed in :python:`main`, but then use other functions that you've made yourself to carry out the main body of work. This fits in better with our testing strategy - each your your functions can be made and tested with :ref:`unit tests <unit_testing>`, and then the more complicated integration tests only need to focus on when everything comes together to in :python:`main`, and :python:`main` is kept very short to help with this. 


Closures
--------
*Closures* are a special type of function, fairly common in Rust programming. We won't cover them more here, but will meet them when we get to those parts of the labs. We'll cover the theory of them then, once you've got a bit more hands on experience of ordinary functions. 