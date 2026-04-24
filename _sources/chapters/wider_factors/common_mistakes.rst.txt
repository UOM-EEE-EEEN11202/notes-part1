.. role:: console(code)
   :language: console

.. role:: python(code)
   :language: python

Common mistakes
===============
We've been teaching programming to first year undergraduates for a number of years now, and so have seen some of the common early mistakes that people tend to make. Here we've listed a few.

This course is intended to take about 200 hours in total. I would tend to think of programming as a 10,000 hour skill. To become an expert takes a long time, and some of the below tend to creep into code because they make it quicker and easier to write in the short term, at the possible cost of building in problems for the future. A challenge in a short course like this is that it's short, you don't get to that future point when these things matter more. 

Indeed, you'll see some examples of the below in different places in these notes. For hard coding, for example, sometimes we're giving just a snippet of code, and it's easier to hard code values into this rather than making you remember the value of something you read a while ago. Similarly, we won't do lots of input validation in the code examples, as it makes the code examples longer harder to see the core concepts. These are shortcuts, but its easy for shortcuts to become habits.


Hard coding
-----------
Hard coding is when a raw value is used, rather than being put into a variable with a meaningful name. For example, say we have a program to calculate the area of a circle. In Python a hard coded version might look like this:

.. code-block:: python

   import math 

   area = math.pi * 5 * 5
   print(f"The area of the circle is {area}")

Here the radius of the circle, 5, is hard coded into the formula. If we want to change this later, we've go to remember to change both appearances of 5. Here they're on the same line and so it's easy to spot that the 5 is present twice, but in longer code the instances could be hundred or thousands of lines apart, and indeed the 5 might appear many times. More robust code will be:

.. code-block:: python

   import math 

   radius = 5
   area = math.pi * radius * radius
   print(f"The area of the circle is {area}")

Now, if the variable :python:`radius` needs to change, we only need to change it in one place. The code is also more readable, as it's clear what the 5 represents.

A variant on this is duplicate code. Continuing the above example, say we wanted to calculate the area of two circles. A hard coded version might be:

.. code-block:: python

   import math 

   radius = 5
   area = math.pi * radius * radius
   print(f"The area of the circle is {area}")

   radius = 2
   area = math.pi * radius * radius
   print(f"The area of the circle is {area}")

Here we have the same equation present twice. If we wanted to change the formula later, we'd have to remember to change it in both places. A better approach is to put the code into a :ref:`function <functions>`.

.. code-block:: python

   import math 

   def circle_area(radius):
       return math.pi * radius * radius

   area = circle_area(5)
   print(f"The area of the circle is {area}")

   area = circle_area(2)
   print(f"The area of the circle is {area}")

In general, the rule (taken from David Thomas and A. Hunt, “The pragmatic programmer,” 2nd edition, Addison-Wesley, Boston, 2019) is *don't repeat yourself*. If you're using the same value more than once, put it in a variable. If you're using the same code more than once, put it in a function. This reduces the chance of mistakes, and makes code easier to read and maintain.

A last variant on the above is hard coded file paths. For example, we might have some code like:

.. code-block:: python

   filename = r"C:\Users\alex\OneDrive - The University of Manchester\work\github\UOM-EEE-EEEN11202\uom-eee-eeen11202-labs-labs\lab-c\frequencies.txt"
   with open(filename, "r") as f:
       data = f.read().splitlines()

Here :python:`filename` is perfectly valid, *on my computer*. If someone else tries to run the code on their computer, or I get a new computer in the future, the location :console:`C:\\Users\\alex\\OneDrive - The University of Manchester\\` may well not exist and the code will fail. This is because it's an :ref:`absolute address <absolute_vs_relative_addresses>` specific to my user name. A better approach is to use a :ref:`relative address <absolute_vs_relative_addresses>`, for example: :python:`./data/frequencies.txt`, which is relative to the location of the code itself, but still relies on the data being put in the correct place relative to the code. It might be preferable to store the data location in a settings file which the code loads in. That way, the code can stay the same in all cases, and if the data location changes, only the settings file needs to be updated. The settings file can contain anything that it user configurable/changeable. 


Data models
-----------
In early code, it's common to have lots of variables. 

.. code-block:: python

   time_1, v_1 = make_example_signal(A=5, tau=0.2)
   time_2, v_2 = make_example_signal(A=5, tau=0.1)

   student1_name = "Alex"
   student1_id = "12345"
   student2_name = "Caitlin"
   student2_id = "24601"

This code will work, and is fine for small cases, but is very repetitive, and prone to errors. A single typo, :python:`1` instead of :python:`2`, and suddenly we're mixing up data. A better approach is to think about the data model, and use a suitable data structure to group related data together. 

For :python:`v_1` and :python:`v_2`, these are both time series. :python:`time_1` and :python:`time_2` might have different actual times in them, but they're representing the same thing - time. A time of 1 s probably means the same thing in both cases. For these, a :ref:`dataframe <dataframes>` might be suitable (particularly if time is actual clock time), or just grouping them into a dictionary or similar.

For :python:`student1_name` and :python:`student1_id`, these are related pieces of data about a student. These might be better grouped into a custom :ref:`object <objects>`, thinking about what data and methods we want to store for each student. You'll see how to make these in `Lab G <https://uom-eee-eeen11202.github.io/notes-part2/chapters/week5/lab_g_stage_1.html>`_. 


Input/output validation
-----------------------
When we load things in from the outside world we can't always trust that the data is in the format we expect! Usually this means user input, or information data file. Once the data has been loaded, there will need to be a number of checks to make sure that the data is valid. These are usually skipped in short introduction code that you get in a course like this, we just let the code fail if the data isn't valid. This is fine when learning, but probably not for anything more critical. 

Most input validation refers to when we get data from the outside world, but remember that for any function, the outside work is anything not in that function. Most functions will have inputs, and will need to have some checks that the input is valid before the function continues.


Error handling
--------------
Following on from the above, a program just crashing when something unexpected happens is fine when it just you as the user. If someone else is using the code, they probably want some more helpful information on what went wrong and why. We'll look at error handling briefly in `Lab H <https://uom-eee-eeen11202.github.io/notes-part2/chapters/week5/lab_h_stage_1.html>`_. As your code gets more complicated, you probably spend more time on input validation, error handling, and other factors than on the core logic of the program itself.


Testing
-------
We'll learn about :ref:`unit testing <automated_testing>` as part of the course. We mention it here as often early code is made with no tests. It is tested *by inspection*, i.e. *it seems to do the right thing*. 


Documentation
-------------
Like the above this is more of a reminder. Early code often has little or no :ref:`documentation <documentation_tools>`. It might have some :ref:`comments <comments>` or :ref:`docstrings <docstrings>`, but these are often sparse and not very helpful. This is a topic which typically isn't covered in a course like this, but the more you write down about what the code is intended to do, and how it goes about does it, the easier it will be for you (or someone else) to understand it later.