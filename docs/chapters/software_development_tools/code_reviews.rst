.. role:: python(code)
   :language: python

Code reviews
============

The previous testing techniques have focused on automated approaches, and on running the code to see what happens. In addition, you can just have another human read your code and give feedback on it! Code reviews are widely used, getting a peer or a manager to look at code in order to improve its quality. 

Say I gave you some code:

.. code-block:: python
    :linenos:

    import math
    
    def main():
        G = 0
        f = 0
        h = 0
		
        G = 7
        f = h + 7
        h = f + 7
    
    
    if __name__ == "__main__":
        main()

What would your feedback on it be?

Some options that you might say are below. (You've not seen all of these topics in the course yet, so you might also like to re-visit this when you're a little further on.)

- There are no comments in the code. It's not at all clear what it's meant to be doing.
- Using upper case G is perfectly fine code, but it's not in-line with our style guide that we're following to keep our code consistent.
- It imports the math module, allowing more maths functions to be used in the code, but none of these are used. You don't need to :python:`import math` just for an addition. If you're not using the functionality, you shouldn't import the module.
- The :python:`+7` appears multiple times. The :python:`7` is thus *hard coded*. Would this be better as a variable, so if it changes, it changes everywhere? Indeed, :python:`G` contains :python:`7`. Should these lines really be :python:`+G`?

This is a simple example, but there's lots of power in getting peer review and feedback on your code. 

.. admonition:: This course

   You can put up your hand in any of the lab sessions to get a graduate teaching assistant to review your code.
