.. role:: C(code)
   :language: C

.. role:: python(code)
   :language: python

.. role:: rust(code)
   :language: rust


Null data types
===============

None/NULL
---------
Many programming languages, but not all, have a data type of :python:`None`. This is the equivalent of *blank* entry. We might have code along the lines of

.. code-block:: python

    exam_mark = None

because we've not got the exam mark available yet. The blank may be filled in later in the code. It's useful to set data to :python:`None` if we don't have it yet, because we can then check, for example at the end of the code. Any students who have :python:`None` as their exam mark didn't sit the exam. (Or there's any error in our code!)

In C/C++ :C:`NULL` is used to the same effect.

It's useful to have a dedicated data type to represent missing data, rather than using something like :python:`0` or an empty string :python:`""`.


NaN
---
NaN stands for *Not a Number*. This is a special floating point value defined in the IEEE 754 floating point standard. It is used to represent missing or undefined numerical data. For example, if we try and compute :math:`0/0`, the result is :python:`NaN`. If you're doing a sum, and the result isn't value for some reason, you'll often get :python:`NaN` as the result.