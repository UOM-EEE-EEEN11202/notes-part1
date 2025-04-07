.. role:: python(code)
   :language: python

.. _objects:

Objects
=======

Objects are where :ref:`functions <functions>` and :ref:`variables <variables>` come together. Let's give an example to show why this is useful, and can help us write correct code.

Example motivating objects
--------------------------

When discussing :ref:`variables <variables>` we had an example of storing the coordinates of a chess piece. Using a list, the *x* and *y* coordinates might be stored as 

.. code-block:: python 

    piece1_pos = ["A", 3]

Let's say our program also has to store the location of the city Manchester. (Maybe there is a chess tournament in Manchester!) This is 53.4808, -2.2426, where these are longitude and latitude numbers. fundamentally, it's still two information items which define the location of the city. We could store these as 

.. code-block:: python 

    manchester_pos = [53.4808, -2.2426]

Then, let's say we have two different things that we want to do:

- Move a chess piece to a different location.
- Lookup the population living within 10 miles of the city centre.

We could write functions to do both of these. We'll switch to :ref:`pseudocode <pseudocode>` for these, as exactly how we would implement these is not critical at this point. The outline of the functions might be

.. code-block:: python 

    def move(item_to_move, x_new, y_new):
        item_to_move[0] = x_new
        item_to_move[1] = y_new
        return item_to_move

    def find_population(location):
        area = draw_10mile_circle_centred_on(location[0],location[1])
        population = search_for_population_in(area)
        return population

These functions would work fine, as long as we always pass the correct variables to them. It doesn't make any conceptual sense to look up the population around a chess piece, or to move the location of the city. There's nothing in the code that prevents us from doing this though. Code such as

.. code-block:: python 

    manchester_pos = [53.4808, -2.2426]
    manchester_pos = move(manchester_pos, "A", 4)

will likely run just fine. The code design isn't helping us to avoid strange bugs. This is of course a simple example, but when there's thousands of lines of code, and multiple different people working as part of a team, you want to try and use the code design to avoid mistakes like this. 

*Objects* are like a *super variable*, they store data, and functions that apply to that data. In these cases, the functions are known as *methods*. In the example above, :python:`move` could be a method for a :python:`chess_piece` object, while :python:`find_population` a method for a :python:`city_location` object. Only chess pieces would be allowed to call :python:`move`, and city locations call :python:`find_population`, and so it prevents people doing incorrect things with data. 

Functions of course are widely used as well as object methods; you just need to think whether the operations are general for whatever input might be provided (make a function), or whether they're specific to a particular data arrangement that you're working with (make an object and method). 


Object basics
-------------
You can make an object by either: defining a *class* which has the code for the data and methods you want; or using *inheritance*, that is, using an existing *class* as a starting point and adding or removing functionally from this. We'll see some examples of making classes in the labs, and won't so won't consider it more here. 

You use a method associated with an object, usually by having dot :python:`.` after the object name, and then the name of method you want to call. In the above examples, you thus might have code along the lines of 

.. code-block:: python 

    piece1_pos.move("A",4)
    manchester_pos.find_population()

Particularly in Python, lots of things are actually objects. For example, :ref:`lists <lists>` and :ref:`dictionaries <dictionaries>` are actually stored as objects, with methods to give them extra functionality. For example

.. code-block:: python 

   piece1_pos_d = {"x": "A", "y": 3}
   piece1_pos_d.keys()

returns the keys that are used with the dictionary (:python:`"x"` and :python:`"y"` here).

.. code-block:: python 

   piece1_pos_d.clear()

removes all of the entries in :python:`piece1_pos_d`.

In general, an object has *attributes* which are accessed by having a dot :python:`.` after the object name. Methods are one example of attributes. 

There are many more methods that can be used with common objects, and we'll see some of these in the labs.