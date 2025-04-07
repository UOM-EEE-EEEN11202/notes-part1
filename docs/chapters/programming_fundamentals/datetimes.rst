.. role:: python(code)
   :language: python

Datetimes
=========
It's very command that we want to represent dates and times in our programs. 

Dates and times have a particular format that humans understand: days, weeks, months, years; hours, minutes, seconds; there are different time zones around the world, and so on. They also have, potentially quite complicated rules around how they work. For example, they also don't necessarily add/subtract in the same way was normal numbers: 6pm plus 8 hours is 2am, the next day, not 14pm. (Even this isn't always true: due to daylight savings we put the clocks forwards/back twice a year, which would lead to a different result).

To allow for this, there are special data types for storing dates and times. There are then lots of functions for manipulating these, such as correctly adding a number of hours to a given time. We won't cover all of these here, but you might want to remember there are lots of functions avaiable for helping to work with dates and times.

Briefly, as Python example, the commands below will make a variable :python:`x` of type datetime. It will contain the date time of whenever the code is run. 

.. code-block:: python

   import datetime
   x = datetime.datetime.now()
   print(x)
