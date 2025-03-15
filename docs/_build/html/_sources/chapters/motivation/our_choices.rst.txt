Our choices for this course
===========================
Programming and software development are very large areas. There are lots of different programming languages, and software development environments that we could chose to study! Here we include some motivations for the choices that we've made in terms of languages. When we go over :ref:`software tools <software_tools>` we'll give the motivations for the different tools we're going to work with. 


Python and Rust
---------------
The course aims to give an introduction to both general purpose programming, and a lower level systems programming language. 

For general purpose programming, Python is the obvious choice. It is very widely used, and commonly listed as the `most widely used programming language <https://www.tiobe.com/tiobe-index/>`_. It is used extensively for machine learning and for data science, as well as more general task automation. Many students will also be starting the course with some previous experience with Python from their school level studies. 

For a lower level language, there is more debate as to the most suitable choice. C, C++, Java and similar are all widely used. Historically, we taught C. Before this we taught Java, and before that it was C. We now focus on Rust. This is due to *memory safety*. We will cover this more later in the course, but briefly, memory safety refers to ensuring that the program can only see areas of memory that are associated with that particular program. It's relatively easy to accidentally write C programs that can access other memory locations and which can be exploited by malicious actors to run code or access data that they shouldn't have access to.

The `National Cyber Security Centre <https://www.ncsc.gov.uk/>`_, and international counterparts, have called for code to have a `roadmap towards being memory safe <https://media.defense.gov/2023/Dec/06/2003352724/-1/-1/0/THE-CASE-FOR-MEMORY-SAFE-ROADMAPS-TLP-CLEAR.PDF>`_. Indeed they state "*Organizations should signal their demand for developers
trained in security and memory safety to colleges, universities, and educational
institutions.*" 

`Google estimate <https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html/>`_ that in 2024 24% of security vulnerabilities in Android were due to memory safety issues. (Down from 76% in 2019 due to their increased such of techniques such as switching to Rust.)

Rust as a programming language has been designed to help minimize memory safety issues. We are thus proactively using Rust to build in memory safe code into your practices from the outset.  


Shell scripting and C/C++
-------------------------
While the above languages represent the main focus of the course, some topics are needed around these in order to give you a solid grounding in programming. 

We will meet the :ref:`terminal or command line interface <cli>` shortly. We use the command line extensively when programming, and *shell scripting* is the process of automating tasks for the command line. It's important to be confident with the command line, and so we'll spend some time developing familiarity with it. 

Equally, there are billions of lines of C and C++ code that have been developed. These will continue to be used and developed for many years to come. While we're going to focus on Rust, it's important to have some familiarity with other compiled languages. It's very likely you'll encounter these languages in other courses at the University of Manchester, and potentially in industry if you go into a software development area. We have a small number of labs on these, to highlight some of the key features of the languages, and give you enough to get up and going if you encounter them in a different course and/or project. 
