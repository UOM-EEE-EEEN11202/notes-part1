Types of programming langugage
==============================

A Computer Science purist might debate the details of the below slightly, but broadly there are 3 types of programming language. There are:

- Markup languages. Such as HTML (the ML stands for Markup Language), XML, LaTeX, Markdown, JSON, yaml. 
- Scripted languages. Such as Python, Matlab, PHP, PowerShell, Bash. 
- Compiled languages. Such as C, C++, C#, Java.

(It's fine to debate this. The aim at this point is to get to right ballpark, not to go into too much depth.)

Markup languages are used for passing text and data around. They rely on having an interpreter which knows what the markup means. For example, in HTML, web browsers know to interpret 
<b>some text</b>
as display "some text" in bold. In LaTeX, the markup for the same thing has a different syntax, 
textbf{some text}. 
JSON, yaml, and similar are for passing data around. For example, JSON stores key-value pairs as: 
{"name": "Alex", 
"office number": 4.018, 
"wears glasses": true} 
which a receiving programme or person can interpret as appropriate. Markup languages are thus very useful for formatting the inputs and outputs of programs in a way that other computer systems know how to use. (Aside: More details on types of programming language.)

Scripted languages work through a series of commands one-block at a time. That is, they execute one line of code, get the results, then the next line, and so on. They're widely used for tasks where there's a fixed order to do things in. For example, in data analysis, first you load the data, then you do some filtering on the data to remove noise and outliers, then you transform the data to highlight the points of interest, then you plot the data, and so on. Scripts are generally quick and easy to write, but slow to run. It's thus a trade-off. They are also relatively sensitive to having run-time errors that the user sees. If there's a mistake on (say) line 50 of the script, the first 49 lines may run fine, and the script only errors out once it gets to line 50. (Aside: More details on types of programming language.)

Compiled languages convert commands into a format the computer can execute, for the entire program, before the code is executed. This process is known as compilation. It means that the code can be optimized, automatically, by the compiler before it is ever run. The code thus tends to run more quickly than scripted code does. The compiler also checks for errors while it's compiling. So, if line 50 is missing a "}", the compilation fails and you have to fix the issue and compile it again before the code can be run. In turn, this means that the code doesn't fail while the user is running the program, and so the user never sees that there was an issue there. 

In practice it's common to use all of these together. Often we use a scripting language such as Python, which is relatively fast to write but slow to execute, to glue together computationally complex tasks which are written in a higher performance language such as C. This gets the best of both worlds. Simple tasks can be done in a quick to write language like Python, while tasks that take a long time to run are written in a more highly optimized language like C. In this course we focus on teaching you the high performance language. 
