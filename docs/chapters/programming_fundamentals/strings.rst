.. role:: console(code)
   :language: console

.. role:: python(code)
   :language: python

.. _strings:

Strings
=======
A string refers to a piece of text. This could be a single character such as :python:`"a"`, or a longer piece of text such as :python:`"Hello world"`. Typically they are entered as being inside either single quotes :python:`'` or double quotes :python:`"`. For example:

.. code-block:: python 

   s1 = "Hello world"
   s2 = 'a'
   s3 = "This is a longer piece of text, known as a string."

Note that our `style guide <https://uom-eee-eeen11202.github.io/chapters/useful_information/style_guide.html>`_ means we'll use double quotes :python:`"`, but Python at least allows either.


String literals
---------------
A fixed string like the above is known as a *string literal*. We're storing only the text we've asked for.


Dynamic strings
---------------
Strings can also be built up dynamically. There are lots of different ways of doing this. For example, we might want to store a person's full name, giving their first name and last name separately. We can do this by *concatenating* (joining together) two strings. For example in Python

.. code-block:: python
   
   first_name = "Alex"
   last_name = "Casson"
   full_name = first_name + " " + last_name  # note the space in between the two names
   
You can also substitute :ref:`variables <single_variables>` into strings. The syntax for this varies between programming languages. In Python, one way of doing this is using *f-strings*, which we'll meet in the Labs. A brief example is

.. code-block:: python 

   age = 21
   greeting = f"Hello. My name is {full_name} and I am {age} years old (still)."


How the computer stores them
----------------------------
How strings are stored in a computer is a little more complex than numbers. We've written a separate page about it to give some details. 

.. toctree::
   :maxdepth: 1

   text_encoding

Consequences of this storage
----------------------------
Working with strings can be a bit harder than you might expect, particularly with lower level languages such as C/C++ or Rust. There are two core drivers of this:

- Different text encodings might be used. C, for example pre-dates UTF-8 and so defaults to ASCII. There are :ref:`libraries <libraries>` that add suitable support for additional characters. 
- We don't necessarily know how long a string is in advance. There may be different numbers of characters (say in a name), and different characters may need different numbers of types to store them. This makes it harder to allocate memory for strings.


Working with strings
--------------------
We'll work with strings a lot in the Labs and so will gain hands on experience of how they work. There are some other factors to take into account:

.. toctree::
   :maxdepth: 1

   working_with_strings
