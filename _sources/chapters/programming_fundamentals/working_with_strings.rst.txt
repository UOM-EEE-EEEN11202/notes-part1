.. role:: python(code)
   :language: python

Special characters
------------------
In addition to representing text (e.g. letters and numbers), there can be other things that we want to include in strings. By far the most common that you'll encounter early is new line. This is entered with :python:`\\n`. :python:`\\n` doesn't display :python:`\\` and then :python:`n` literally. Instead, it enters a new line. So:

.. code-block:: python

   print("hello\nworld")

displays as

.. code-block:: console

   hello
   world

There are a number of such special characters. For example, you might see :python:`\t` to represent a tab (indentation).


Escape sequences
----------------
A number of characters can't be entered into a string directly. For example, a quote, :python:`"` is used to represent the start/end of a string. If we want to include a quote symbol inside a string, you need to put a backslash :python:`\\` before it. For example:

.. code-block:: python

   quote = "Alex said, \"Hello world.\""
   print(quote)

Otherwise, the first quote symbol would be mis-interpreted by Python as the end of the string.

There are a number of characters that need to be escaped this way and you might encounter in your work. For example, to include a backslash :python:`\\` in a string you need to escape it as :python:`\\\\`.

Using the backslash :python:`\\` before the wanted symbol is known as an *escape sequence*. In most cases a backslash before a character means that the following character is to be treated specially. Sometimes other symbols are used as the escape character, such as a curly brace :python:`{` or percentage symbol :python:`%`.


Raw strings
-----------
If you have a string which contains lots of characters that need escaping, it can be error prone to keep adding backslashes, and can make the string hard to read. Python, but not all programming languages, allows you to enter *raw strings*. If a string starts with :python:`r` before the opening quote, then all the characters in the string are treated literally. So, you can write

.. code-block:: python

   quote = r"Alex said, "Hello world.""
   print(quote)

It can help make strings more readable. 


Number formatting
-----------------
Often in a string we want it to display numbers, which might be read from a variable. We might want the same number to be displayed in different ways. For example, we might want 0.12345 to be displayed as 0.12 (i.e. to 2 decimal places), or 0.123450 (to 6 decimal places). Or, we might want 0.001 to be displayed as 1e-3 (i.e. in scientific notation). We can add a *format specifier* to allow this. 

We won't cover over all of formatting choices here. There are many choices available and well documented in the `Python documentation <https://docs.python.org/3/library/string.html#formatspec>`_. A few examples are shown below.

.. code-block:: python

   value = 0.12345
   print(f"Value to 2 decimal places: {value:.2f}")
   print(f"Value to 6 decimal places: {value:.6f}")
   print(f"Value in scientific notation, with two decimal places: {value:.2e}")