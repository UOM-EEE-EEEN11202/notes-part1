.. role:: console(code)
   :language: console

.. _automated_testing:

Unit and integration testing
============================

General principles
------------------

Debugging is one aspect of testing, generally focused on making your code fundamentally run. Testing in general, is a much wider topic. You need to thoroughly test your code, running it multiple times, to check that it behaves in the way that you want it to. Whenever possible, we don't wait around for users to tell us about bugs in our program. Instead we write automated tests that can tell us if anything is broken. 

For example, your code may accept a wide range of inputs, or have a range of different options. It's not uncommon for code to work in a large number of cases, but fail in some corner cases. Maybe you weren't expecting a filename which includes a :console:`!`. Your code may work fine, except for cases when a :console:`!` is present in a filename passed to it. 

It's hard to test every possible input, but you probably want to make a *test suite*, which automatically passes a wide range of filenames (in this example) to your code to check that it works. 

Thus, for non-trivial code, you often have to actually write two different parts:

- The actual code of your project that implements your wanted functionality.
- A *test wrapper* (or *test harness*) which can run your code and check that, for various cases that are important to you, the code actually does what you want.

Note that these different parts don't necessarily have to be in the same language. Also, you may need to make a test suite, to test the wrapper!

Within this testing is usually broken down into two stages: *unit testing* and *integration testing*. 


.. _unit_testing:

Unit tests
----------

We noted previously that a software projects in practice can be :ref:`millions of lines of code long <files_folders_filesystems>`. Testing all of this in one go is hard! We need to break it down into smaller pieces, to help compartmentalize where any issues might lie.

To do this, we try and write blocks of code in as small chunks, known as *units*, as possible. We then connect these units together to make a bigger program. Each unit is less code than a big complex function, and easier to test and debug in isolation. 

*Unit testing* refers to testing each of the individual blocks in isolation. The idea is that if each block works, then any issues later can only be due to the interaction of different blocks. It thus helps localize where the issue might be, so you know where to look when investigating issues.

There's no hard rule for what or how big a unit is. A decision needs to be made during the :ref:`software architecture stage <software_architecture>` of what would be suitable sub-blocks to split the design and testing into. 


.. _integration_testing:

Integration tests
-----------------

*Integration testing* comes when you connect all of your different blocks together to check that the larger function works as expected. Generally, you have a list or database of different inputs to provide, or tests to run, where you know what the output should be, so you can check whether it's working. 

In random testing you generate a set of test inputs randomly. In directed testing you enter explicit test inputs that are important to you to check.



Assert statements
-----------------

To help with the above, there are *testing frameworks* such as `pytest <https://docs.pytest.org/en/stable/>`_ to help run the above processes. We'll see some of these in the labs.

The general building block for testing is an *assert* statement. This might look something like

.. code-block:: python

    assert x == 0

This assert statement means *at this point I the programmer know x should be 0. If it is, carry on as usual. If it's not, flag that the test has failed*. 

There are lots of different types of assert checks that can be used, Generally they do rely on you having some knowledge (for your given test input) of what the code should ideally be doing at a particular point. 

.. admonition:: This course

    We will spend some time in the labs looking at unit testing in both Python and Rust.