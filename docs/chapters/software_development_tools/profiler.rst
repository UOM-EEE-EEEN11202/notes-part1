.. role:: console(code)
   :language: console

Profiler and computational complexity
=====================================

Profiler
--------
When we looked briefly at :ref:`computer architecture <computer_hardware>`, we noted that there were a number of potential bottlenecks present which may limit how quickly the code can run. It may be that the code is limited by the processor, or by the amount of memory that is present, or by the input/output bandwidth. 

For all code, it's useful to know which resources are being used the most. This allows you to potentially change your code to make it faster, or use fewer resources, or to compare how many resources two different approaches require. For performance critical applications this is very important.  

A *profiler* analyses your code to generate a report on resource usage that you can use to inform the design or optimization of your code. 

For example, in Python you might use

.. code-block:: python

    import cProfile
    cProfile.run('<Python code here>')

More generally, you might install a profiler outside of the IDE environment and use it as an independent tool. :console:`perf` is a common tool if using Linux. Intel make a free profiler available called `VTune <https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html>`_  which runs on Windows, macOS, and Linux.

.. admonition:: This course
   
   We're not going to make use of profilers, but you might like to remember they're a tool you can investigate and make use of if you find your code takes too long to run or is too resource intensive.


Computational complexity
------------------------
In addition to analyzing the code you actually have, it's common to think *conceptually* about what the computational complexity is. We won't focus too much on this, but it is often useful to think about how well an algorithm, or code implementing that algorithm, will scale as more data is passed to it.

In :ref:`pseudocode <pseudocode>`, if you have an algorithm:

.. code-block:: python

	count = 0
	elements = [1, 2, 3, 4, 5]
	for each element in elements
	    count = count + value_of_current_element

this will scale linearly. If there were 10 values in the elements array, rather than the current 5, we'd expect it to take twice as long to execute. This is because the addition will take the same amount of time in every case, so the complexity is dominated by how many times the for loop has to run. If we double the number of values present, we double the number of times the loop executes. Doubling the size of the input, doubles the execution time, and so the complexity is scaling linearly with the input size.

Typically we use *Big O* notation to represent complexity. If :math:`n` is the number of values present in the elements array, the above example would be :math:`O(n)`. The complexity just depends on the number of elements present. 

Different code could to be :math:`O(n^2)`. Here, doubling the elements from 5 to 10 would result in code which takes 4 times as long to run :math:`(10^2/5^2)`. Code which is :math:`O(n^3)` or even :math:`O(n!)` is possible, if they may take a long time to run when you have lots of data! With some thought, lots of algorithms can be written to be :math:`O(n \log n)`, but this might require some effort and not be the first approach you come up with.

.. admonition:: This course

   In terms of this course, computational complexity is a relatively advanced topic. It's more something to be aware of than something we'll use lots. It affects the design stage of code, possibly more than the implementation stage where you can use the profiler. If your code is going to take a long time to run, at the design stage you need to consider both the architecture, and the potential computational complexity of the approach. Even if it's just a rough estimate, it can help you discount some potential approaches early on. We won't look at this in depth though.