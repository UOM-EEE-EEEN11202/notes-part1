Programming fundamentals
========================

Every Programming language is different, and each works in a slightly different way. This is why there is, and why we learn, more than one programming language. Different languages have different pros and cons, and may better suit or not suit particular problems or constraints that are present.

Nevertheless, there a wide number of general concepts that apply across our different types of programming. Sometimes there are variations in different languages, and sometimes the same underlying concept is given different names in different places, but the approach is similar.

This part of the notes introduces some of these concepts, so that we can think about them *in theory* before getting to practicing them in the lab. We'll mainly give examples in Python, but will also use :ref:`pseudocode <pseudocode>` so we can focus on the underlying concepts rather than necessarily what's needed to make them work in practice. 

Some of the later topics, those from :ref:`stack and heap memory <stack_and_heap>` and after, are relatively advanced and relate more to the latter half of the course on Rust and lower level languages. You may like to revisit these later in the course. 

In any program, there are two key things that we need: *data* the information we're working with; and *operations* we can do to that data to manipulate it, extract information from it, or convert it in-line with whatever our needs are. The basic unit of storing data is a :ref:`variable <variables>`. (There are then other types we'll get to later.) The basic unit of code to manipulate data is a :ref:`function <functions>`. We're going to introduce functions first, but of course this makes some use of variables, and so you might need to go back and re-read functions once you've also read about variables. 

.. toctree::
   :maxdepth: 2
   :hidden:

   programming_fundamentals/scripts
   programming_fundamentals/functions
   programming_fundamentals/mutability
   programming_fundamentals/variables
   programming_fundamentals/objects
   programming_fundamentals/data_types
   programming_fundamentals/conditionals_and_loops
   programming_fundamentals/scope
   programming_fundamentals/design_patterns
   programming_fundamentals/copies
   programming_fundamentals/stack_and_heap
   programming_fundamentals/pointers
   programming_fundamentals/lifetimes
   programming_fundamentals/advanced_topics