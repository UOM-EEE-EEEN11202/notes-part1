.. role:: console(code)
   :language: console

.. role:: python(code)
   :language: python



Data types
==========

Overview
--------
Behind the scenes, computers work in *binary*. Everything is stored as either a :console:`0` or a :console:`1`. Many of the details of this are not important for this course, you'll go into detail on binary in your digital electronics courses. However, we always need to remember this, as it shapes how and why computers and programs work the way they do.

For our programs, we need a way of going between the :console:`0`'s and a :console:`1`'s that a computer works with, and the data a human works with. We're used to dealing with numbers (e.g. 0, 8, 22.3), or text (e.g. "*hello*"), or dates (05.11.1955), and many other formats. 

To do this, there are two things built in to our programming. Firstly, there is an agreed on *standard*. If we all agree that :console:`01001101` represents the letter :console:`M`, then we can work with that. There are well established standards for how computers represent common types of data (e.g. IEEE/ISO/IEC 60559 for storing numbers that have decimal points). In general, we won't worry about these in this course. The computer knows the standard for us, and we only need to go into a little depth on the following pages.

Secondly, each thing we store in our code, whether via a variable or in an object, is given a *data type*. The program is given some additional information to help it know what kind of information is being kept. For example, in Python, if you have

.. code-block:: python 

    name = "alex"

the double quotes :python:`"` help indicate that this is storing text. 


Common data types
-----------------
There are a number of common data types, and we'll introduce the properties of some important ones on the following pages. It's not necessary to know all of the details of these, but it is important to have some understanding of how our data is being used by the computer *under-the-hood*. Having some familiarity will help you debug when you have issues with your data.

.. toctree::
   :maxdepth: 1

   booleans
   integers
   floating_point_numbers
   text_encoding
   none_some
   datetimes
   dataframes


Dynamically typed vs. statically typed
--------------------------------------
In general, Python is *dynamically typed*. That means, it looks at our code for us, and automatically works out which data type to use and this can change on-the-fly. In contrast, Rust is *statically typed*. We have to explicitly say what data type to use for a piece of data. For our purposes, you may see *weakly typed* and *strongly typed* being used in place of dynamic and static.  

Being statically typed makes it more work for the programmer, as you have to enter this information each time you define a new variable (and think about what you want the data type to be!). The resulting program can then run faster, as the computer doesn't have to figure out the data type for you. It can also help avoid mistakes. If you try and put, say, text in a variable expecting a number, this is easy for the computer to automatically spot that there'a bug in the code. 

.. admonition:: Aside

    While dynamically typed, Python has the concept of *type hints*. When we make a variable, we can state the data type we think it should have, in addition to giving the name and the value of the variable. The example as we had in :ref:`variables <single_variables>` might now look like

    .. code-block:: python 

       num: int = 2
       pi_ish: float = 3.1415
       name: str = "alex"
       check: bool = True
       blank: None = None

    Similarly for functions, you can add :python:`->` to flag the data type of the function output. Our example from :ref:`functions <functions>` might now look like

    .. code-block:: python 

       def add_and_multiply(a: int, b: float) -> float:
            c = 3 * (a + b)
            return c
    
    Here :python:`a: int` indicates that it's expecting input :python:`a` to be an integer. In contrast, input :python:`b` is expected to be a float.  
    :python:`-> float` indicates that the output, :python:`c` in this case, should be a floating point number. 

    These *hints* are intended for programmers looking at or using the code. Particularly for large code bases or multi-developer teams, they can help people understand the code and use it correctly. There are also automatic tools which can flag if there is a conflict in the types being hinted at.

    As this is an introductory course, we won't look at, or enforce, type hinting any further beyond this aside. For Python coding however, it is generally considered good practice to include type hints in your code. 
