.. role:: console(code)
   :language: console

.. _pseudocode:

Pseudocode
==========

The tools mentioned so far are software programs that help you write correct code. There are also tools and techniques that will help you plan and design your code. The main one to mention here is *pseudocode*. This isn't a software tool, it's an approach to planning your code before you write it in detail.

Pseudocode is a detailed, but readable, description of what you want your program to do. A very high level example might be

.. code-block:: console

    Decide to take train
    Pick which train to get
    Buy ticket
    Get tram to Manchester Piccadilly station
    Get on train

This a long way from actual code that gets a robot to take a train(!), but is a start towards some of the key functional blocks that are going to be needed.

As a lower level example, when considering the profiler we had:

.. code-block:: python

	count = 0
	elements = [1, 2, 3, 4, 5]
	for each element in elements
	    count = count + value_of_current_element

This isn't valid Python code. It won't run if you try to put it in a :console:`.py` file directly. Instead, it is (hopefully) fairly easy to read and understand. It helps you to explain what you want your code to do, before you then go away and write the detailed code. 

You can do a lot of your code design at the pseudocode level, without having to worry about things like: should there be a bracket here?; or is this value initialized correctly?; or other details. The details are important, but come later.

Beyond this, there are no rules or standardized syntax around pseudocode, it's whatever you find useful. You might write quite high level pseudocode which just gives the *gist* of what has to be done, or you might write very detailed pseudocode which is very close to actual code. Both have their places. Pseudocode is a way to writing down what you want your code to do, in order to help with the design and documentation phases. 

.. admonition:: This course

   We'll use pseudocode in a number of places where it's helpful to describe the concept of what we want to do, without some of the *boilerplate* code that would actually be needed to make it work in practice (and where having such extra details would make it harder to see the core underlying concept).

   In general, we don't have any pseudocode specific tasks for you to do, but you might like to use pseudocode to rough out a solution before coding it; particularly for some of the bigger tasks we give you.