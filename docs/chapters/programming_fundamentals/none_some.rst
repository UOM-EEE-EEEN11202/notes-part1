.. role:: C(code)
   :language: C

.. role:: python(code)
   :language: python

.. role:: rust(code)
   :language: rust

None/Null and Some
==================
Many programming languages, but not all, have a data type of :python:`None`. This is the equivalent of *blank* entry. We might have code along the lines of

.. code-block:: python

    exam_mark = None

because we've not got the exam mark available yet. The blank may be filled in later in the code. It's useful to set data to :python:`None` if we don't have it yet, because we can then check, for example at the end of the code. Any students who have :python:`None` as their exam mark didn't sit the exam. (Or there's any error in our code!)

In C/C++ :C:`NULL` is used to the same effect.

Rust introduces a :rust:`Some` type. This lets you check that you have got something, without necessarily caring what it is at that point in time. It might be an integer, or a string or something else. :rust:`Some` just lets you represent that you have something present. This can be really helpful when you have multiple data types that a function might work with.