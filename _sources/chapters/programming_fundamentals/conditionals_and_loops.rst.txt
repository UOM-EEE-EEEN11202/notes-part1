.. role:: python(code)
   :language: python

.. role:: C(code)
   :language: C

Conditionals and loops
======================
Once you have data, stored in a variable or an object, and ways to manipulate or modify or interact with that data via functions or methods, the main art of programming is plumbing together the different steps that are needed in order to achieve the required overall functionality. There are several more common programming concepts to help you achieve this.


If/else statements
------------------
If/else statements allow you to execute code only if certain conditions are met. For example, the code below

.. code-block:: python

    a = 0
    b = 3
    if b == a:
        c = 7
    elif a > b:
        c = -7
    else:
        c = 0

will set the value of :python:`c` differently depending on the values of :python:`a` and :python:`b`. Here there are only three branches, but there could be as many as you want. 

The :python:`else` case acts as catch all, the default if none of the other conditions match. You can use this to help catch error cases. For example, you might re-write the above code more like:

.. code-block:: python

    a = 0
    b = 3
    if b == a:
        c = 7
    elif a > b:
        c = -7
    elif a < b:
        c = 0
    else:
        raise Exception("Something must have gone wrong!")


.. _for_loops:

For loops
---------
It's very common that we want to perform the same operation multiple times. For example, maybe we want to load all of the marks that a student has obtained across the labs and sum them. We need to loop through the marks for each lab and add them to a running total. 

We'll start with an example of a loop using the C programming language, as it helps illustrate the operation. Here, the basic syntax is:

.. code-block:: C

   for (start_condition; end_condition; step ) { 
       // statements to run
   }

such that an overall loop might look like:

.. code-block:: C
   :linenos:

   #define N 10
   int lab_marks[N] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
   int total_mark = 0;
   for (int i = 0; i < N; i++) {
       total_mark = total_mark + lab_marks[i]; 
   }

Here :C:`i` is the *loop variable*, the variable used to keep track of which iteration of the loop we are on. Here is it called :C:`i`, but we can use any valid variable name. The first time the for loop is run, :C:`i` is set to 0. The second argument, :C:`i < N`, gives the control statement. The loop will continue to execute while this statement is true. Note that here :C:`N` is 10, and must match the number of entries in lab_marks or you'll get bugs when the program runs. The third argument, :C:`i++`, gives the equation for modifying the loop variable at the end of each iteration. :C:`i++` means :C:`i` increases by 1 each time, so the code looks at :C:`lab_marks[0]`, then :C:`lab_marks[1]`, and so on.

The above works well, and is very common. The main limitation is that you the programmer have to know how many entries are present in the array. In the above example we hard coded it to be 10. If we added or removed another lab, the code would have to change. (Indeed in this example the code would have to change in two places: the value of :C:`N` on line 1, and the number of entries in :C:`lab_marks[N]` on line 2.). 

Wanting to work with all of the elements that are stored is such a common thing to do that many other languages provide an improved syntax which means you don't need to look up how many entries are present. They use *iterators* to automatically makes the start/stop/step conditions for us. The same loop in Python would look more like:

.. code-block:: python

   lab_marks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
   total_mark = 0
   for mark in lab_marks:
       total_mark = total_mark + mark

(Note that Python also provides a :python:`.sum()` method that we could have used in this case rather than writing our own code.)

:python:`mark` is set in turn to :python:`lab_marks[0]`, :python:`lab_marks[1]` and so on. We won't go into the details of *iterators*, most objects we'll work with already make them for us. They simplify writing the loop as we don't need to count ourselves how many entries are present. 

Note that if you need to keep track of how many times the loop has run, you can use

.. code-block:: python
    
   lab_marks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
   total_mark = 0
   for i, mark in enumerate(lab_marks):
       total_mark = total_mark + mark

to provide a variable :python:`i`, like we had in the first C example.


While loops
-----------
While loops operate in a similar manner. The code in the loop runs multiple times, until some condition is no longer met. For example, we might write the above example as

.. code-block:: python

   lab_marks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
   total_mark = 0
   i = 0
   while i < len(lab_marks):
       total_mark = total_mark + lab_marks[i]
       i++

In general we can accomplish the same functionality using either a for loop or a while loop, they just need writing in slightly different ways. 

There's thus some aspect of style/preference for which you use. While loops tend to be used when waiting for an operation to complete or a user to provide some input. For example

.. code-block:: python

   while button_pressed:
       do_operation()


Breaking loops
--------------
There are many more functions/possible actions to customize the operation of conditional statements and loops.

- :python:`pass` can be used if you don't want any operation to take place. (Maybe you've not implemented that code yet, or there's a case where no action is needed, but it's simpler to still have the code checking for such a case being present.)
- :python:`continue` in a for or while or loop will stop the execution of the current iteration, and jump to the next one. That is, if :python:`i` was 7, it would straight way change it to 8 and jump back to the top of the loop.
- :python:`break` causes the if statement or for/while loop to stop. The program execution will jump put of the loop and then keep going with whatever comes next. 

There are lots of variations on the above, and the precise syntax differs between different programming languages, but essentially all have the same basic underlying concepts. We'll practice these in the labs. 
