Types of programming language
=============================

A Computer Science purist might debate the details of the below slightly, but broadly there are 3 types of programming language. There are:

- Markup languages. Such as HTML (the ML stands for Markup Language), XML, LaTeX, Markdown, JSON, yaml. 
- Scripted (interpreted) languages. Such as Python, Matlab, PHP, PowerShell, Bash. 
- Compiled languages. Such as C, C++, C#, Java, Rust.

(It's fine to debate this. The aim at this point is to get to right ballpark, not to go into too much depth.)


Markup languages
----------------

Markup languages are used for passing text and data around. They rely on having an interpreter which knows what the markup means. For example, in HTML, web browsers know to interpret 

.. code-block:: html

   <b>some text</b>

as display "some text" in bold. In LaTeX, the markup for the same thing has a different syntax, 

.. code-block:: latex

   \textbf{some text}

JSON, yaml, and similar are for passing data around. For example, JSON stores key-value pairs as: 

.. code-block:: JSON
   :linenos:

   {"name": "Alex", 
    "office number": 4.018, 
    "wears glasses": true} 

which a receiving programme or person can interpret as appropriate. Markup languages are thus very useful for formatting the inputs and outputs of programs in a way that other computer systems know how to use. (Aside: More details on types of programming language.)


Scripted languages
------------------

Scripted languages run code by working through a series of commands, one line at a time. That is, they execute one line of code, get the results, then the next line, and so on. They're widely used for tasks where there's a fixed order to do things in. For example, in data analysis, first you load the data, then you do some filtering on the data to remove noise and outliers, then you transform the data to highlight the points of interest, then you plot the data, and so on. 

Scripts are generally quick and easy to write, but slow to run. It's thus a trade-off. They are also relatively sensitive to having run-time errors that the user sees. If there's a mistake on (say) line 50 of the script, the first 49 lines may run fine, and the script only errors out once it gets to line 50. 


Compiled languages
------------------

Compiled languages convert commands into a format the computer can execute, for the entire program, before the code is executed. This process is known as compilation. It means that the code can be optimized, automatically, by the compiler before it is ever run. 

The code thus tends to run more quickly than scripted code does. The compiler also checks for errors while it's compiling. So, if line 50 is missing a "}", the compilation fails and you have to fix the issue and compile it again before the code can be run. In turn, this means that the code doesn't fail while the user is running the program, and so the user never sees that there was an issue there. 

In practice it's common to use all of these together. Often we use a scripting language such as Python, which is relatively fast to write but slow to execute, to *glue* together computationally complex tasks which are written in a higher performance language. This gets the best of both worlds. Simple tasks can be done in a quick to write language like Python, while tasks that take a long time to run are written in a more highly optimized language. 


.. admonition:: Asides

   Two minor asides are relevant here for completeness. 

   Firstly, technically markup is only for text. (So languages like HTML and Markdown.) JSON or yaml (as examples) for passing data around aren't markup. I think it's useful to badge them under the same heading of: a structured form for sending something around so the receiver knows what they're receiving and what they need to do to interpret it; which I've called markup. In any case, the ML in yaml stands for markup language (with the exact meaning having changed over time). 
   
   Secondly, today, many scripted languages use *Just-In-Time Compilation* to help them run faster. Rather than running as a pure script, line-by-line; when run, first a quick compilation is carried out to check for errors and any optimizations that can be performed, before it is then run line-by-line. If you have an error on line 50, the Just-In-Time Compilation will probably spot this, and refuse to run anything before it's fixed. It's a technique used to speed up scripts, but they are usually still slower than a fully compiled language.
