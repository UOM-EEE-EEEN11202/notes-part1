.. role:: python(code)
   :language: python

.. role:: cpp(code)
   :language: cpp

Lifetimes, borrowing, and "modern" approaches
=============================================
As we mentioned in :ref:`pointers <pointers>`, when writing low level code we need to think about the *lifetime* of the items we're working with. 

If we open a file, we need to remember to close it when we're done. Once it's been closed, we then can't read from the file again. If we try to read from a closed file, we'll get an error. If we don't close the file, we'll accumulate more and more baggage as the program runs until we eventually run out of resources on the computer.

If we use a section of memory, we need to remember to give it back when we're done. Once we've given it back, we then can't read from it again. Once we've given memory back, it might be used for some other purpose. If we try to read the same memory location again, the read will likely work - it is still a valid memory location - but if another program is now using that location we'll get incorrect data coming back. 

This sort of, using a resource, giving it back when we're done, then remembering we don't have it any more it quite common. If might be using a chunk of memory, a network resource, or something else. In general it's up to us to think about the lifetime of a resource and when we can validly use it. Making mistakes with this are some of the most common programming errors. 

Sometimes, and particularly in Rust programming we refer to *borrowing* a resource. Rust includes a *borrow checker* to help make sure that if we borrow something, we give it back too. 

In general, in older programming languages such as C, freeing up resources once finished with is up to the programmer. You have to include explicit code to do this. More modern languages do this for you. :ref:`Smart pointers <smart_pointers>` were an example of this. Actually, there are many examples. In Python we open a file using the :python:`with` command as

.. code-block:: python

   fn = "filename.txt"
   with open(fn) as my_file:
       my_file.read()

This will automatically close the file for us when it's finished with. Python does have a :python:`close()` command, but we don't need to explicitly include it in our code.

Some people argue, with good merit, that when starting programming we should teach you to write more explicit code so that you get used to opening and closing resources. So, using :python:`open()` follow it by :python:`close()`. Or, if using raw pointers in C++, making a pointer :cpp:`int* ptr = new int(77);` and then deleting it when done with :cpp:`delete ptr;`. 

That's not the philosophy this course takes. Features have been added to programming languages to stop people from making these common mistakes, and so we're going to teach you to use them. It's important though that you don't forget that this is the computer doing some tasks for you. If you borrow a resource, you always need to remember to give it back. If you're not doing explicitly, make sure the language is doing it for you.

The slight exception to the above is C++. This is both a relatively old programming language, and a modern language. You may hear people refer to *modern* C++. This means using features such as smart pointers, which weren't available when the language was first introduced in 1985. C++ is updated today every three years. There's no hard rule, but *modern* C++ generally refers to using C++11, introduced in 2011, or later. 

Modern C++ has a wide number of features, such as smart pointers and *templates* to help avoid previously common programming errors. *Resource Acquisition is Initialization (RAII)* is an important part of modern C++. Again, this refers to the concept that if you borrow a resource, you must give it back. RAII approaches automatically give the resource back to the computer when the block of code goes out of :ref:`scope <scope>`.