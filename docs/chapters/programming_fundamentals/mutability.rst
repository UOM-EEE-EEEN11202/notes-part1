Mutable vs. immutable
=====================

Before looking at :ref:`variables <variables>`, a brief note on *mutability* is needed.

Being mutable means that the value can change. Being immutable means that it can't. We'll make reference to mutable variables and immutable variables in quite a few places, and they are very important when you get to Rust programming. 

It might sound a bit odd to have an immutable variable, vary implies it can change but being immutable means it can't. 

This is actually quite common in programming - we can use it to help force us write code which is error free. 

Say I have some code which loads in the list of students taking the course, and their marks. This data is variable - when the course is run next year there will be a different list of students taking the course. On any individual run of the code though the list of students is immutable - I don't want to accidentally add to delete any students from the class roster! By making the data as immutable it makes it easier for the built in tools to detect whether the code has any errors which means it tries to change data that should be fixed. 

In our programming it's quite common that we want to take steps like this, using our knowledge of the problem to restrict the code, to help ensure the code is correct. 