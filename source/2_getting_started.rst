Getting started
===============

Introduction
------------

There are two aims in this part.

Firstly, it's to get a basic programming environment set up and working. By tradition, the first thing to do when learning a new programming language is to write a simple program to display "Hello World". We'll look at doing this, and the basic structure of a C program that you need to follow.

Secondly, it's to learn about some of the tools that are available to help you carry out software development. Rather than launching into coding, the aim is to first have an awareness of what tools are out there to help you do it well, and minimise bugs and mistakes in your code. It's important to learn about how to do software development, before you start doing software development, to avoid bad practices creeping in from the outset. We'll thus look at this aspect first.


Where you'll use this knowledge
-------------------------------

The content here underpins all of the rest of the course and will be widely used in any practical programming you do. 

Some items, such as the IDE, debugging, and version control you will use widely in the labs, and as you do your own software development. Some other topics, such as environment control, we won't use directly in this course. Rather, they are included briefly so that you're aware of them. You will likely use such tools if you move into software development full time, and the aim is to make sure you know they exist so you have an awareness if they become important later.




How we actually write software
------------------------------
While the previous section goes through the main steps, in practice there are a number of other steps that are needed in order to write high quality software. Many of the tasks relate to documentation. These often get skipped over in small projects, but it's important to have an awareness of the actual processes involved. 


Software lifecycle
~~~~~~~~~~~~~~~~~~
The software lifecycle refers to us considering all of the steps involved in writing, deploying, and maintaining code. There are international standards that set out the steps that people/teams/organisations should go through:

- ISO/IEC/IEEE 12207 covers general software.
- IEC 62304 covers medical device software. 

Generally, the higher risk the software (e.g. for medical devices, for planes vs. for toasters, for TVs) the more steps, documentation, and testing are required. 

We won't go through these international standards in detail, but will briefly overview the steps in the following sections. Some will come across as common sense, but as the saying goes, "common sense isn't always that common". It's easy to skip some steps, or to do them too briefly, and build up problems that make the code hard to maintain.


Requirements capture
~~~~~~~~~~~~~~~~~~~~
The first step is to have a good understanding of what functionality the program has to have. This includes an understanding of what constraints are present. 

Documenting the requirements or specifications, before you start, is essential for any project. This is important to ensure that everybody is on the same page, and to define what success looks like and how you will know whether you've achieved it or not. You don't want cases where (say) you think your software only has to run on Windows, but your customer thinks it has to run on both Windows and macOS. Or (say) a case where you're detecting number plates from vehicles in a car park, and you think this only covers cars but your customer thinks this covers both cars and motorbikes. Or, you think you need to detect 99% of the number plates correctly in order for the software to be successful, but your customer thinks it needs to be 99.9%. 

You can always change the requirements later on if the project evolves in scope, but this is changing from a fixed established base, and you can ask for more time or money or resources to support the change. In the example above, the software that the customer wants is likely to take much longer to develop and test; and so it will cost more money. It's very common for clients to implicitly or explicitly want feature creep. That is, more and more features to be added but without giving you any more time or money for adding them. Having a formal requirements capture, that they've agreed to in advance, helps stop this from happening. 

Sometimes there are factors that you won't know the answer to until you have an initial proof of concept in place and can do some preliminary tests. (In the example above, preliminary tests might show that 90% is the best you can get in real-world settings so the performance target will need revising.) Sometimes things are just overlooked. (In the example above, is run time important?) There are formal techniques to guide requirements capture and help make sure that you don't forget any important factors. Overall though, the most important thing is to write down the requirements that you do have so that they are fixed and agreed upon as best possible.


Software architecture
~~~~~~~~~~~~~~~~~~~~~
Software architecture refers to how you choose to split up your code and implement the required functionality. You could put everything in one big file, but that probably isn't the best way to do it! Usually we split the code up by function. Continuing our example of detecting car number plates, maybe you have one unit of code which identifies where a number plate is in a camera picture, and another unit of code that does letter/number recognition on this. Each part has its own distinct aim, and they can potentially be developed separately (for example by different developers) before being brought together.

There are lots of decisions that need to be made here. How do the two bits of code talk to each other? For the code which identifies where a number plate is, is the output a set of coordinates telling the other function where to look, or is it an image which has been cropped from the main picture to show just the area of interest? Both are potentially fine, you just need to agree which you're doing. 

Defining the architecture of software typically involves:

- Within the overall goal of the program, defining what the main functions are and how these will be grouped together. 
- Defining what the interfaces between these different functions will be. 

For a large problem, this then gives you a high level blueprint to build your more detailed code against. In the same way that you wouldn't start building a house without a reasonably detailed plan of what you're going to build, you shouldn't start writing complicated code without a reasonably detailed plan of what it's going to look like. It helps makes the task more manageable by breaking it down into smaller chunks, and makes it easier to identify where in the code particular functionality is implemented (because you can look it up in the architecture rather than the more detailed code). 

Again, the architecture wants to be written down, so that everybody knows what it is they're trying to build. Design it, and then code it. Not the other way round. (Any architecture will probably be iterated several times during the process of actually writing the code, adding more detail each time, and that's fine.)



Testing and debugging
~~~~~~~~~~~~~~~~~~~~~
Very few programs work first time! This could be due to a simple mistake like a typo, or due to something quite subtle that you weren't anticipating happening. Often a program will largely do what you want, but in some cases will crash or do something unexpected, and these corner cases need investigating. Debugging is the process of going through your code to see what happens in particular cases, and resolving issues so that the code works satisfactorily. 

You'll soon find that debugging takes as long, if not longer, than writing the code in the first place! Some engineers specialise in verification and validation. That is, testing code rather than developing it in the first place. 

There are lots of tools and techniques to help you with testing and debugging, and you'll use some in this course. 


Release, support, maintenance, and bug fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once all of your development has been done, and the code compiled and tested, an end product can be shipped to customers. In any non-trivial project, they'll probably find more bugs! Testing is hard, and if your software is being used on thousands or millions of devices, each with a slightly different setup, it's extremely hard to detect everything in advance. (This isn't an excuse for shipping poor quality, bug-riddled code, just pragmatism. I'm sure we'll all familiar with encountering bugs in programs we use on a computer.)

An important part of the software lifecycle is thus supporting your application after it's been released. Typically programs are supported for a number of years, and customers can look up how long this is. Within the support period, new versions will be released, with bug fixes, possibly some small feature updates, and any security related updates. After the support period the software then falls out of support and the customer needs to get (possibly buy) a new version if they want to get the latest fixes. It's not uncommon for customers to pay more money for longer support periods, so that they can get bug and security fixes without having to completely update or change the software. 

This support and maintained needs to be factored in when planning a software project. It may need fewer resources (people, money) than making the program in the first place, but it's going to need some. Writing code which is easy to read and maintain is very important, as it may not be the original writer who has to go in and hunt down obscure bugs many years later!


Documentation
~~~~~~~~~~~~~
Documentation comes towards the end of the list here, but really it underpins all of the aspects of writing software. The code, the .c file(s), doesn't stand in isolation. It's paired with documentation which describes the requirements, the architecture, the testing strategy and results, and so on. 

Writing a program is a design task - there are usually lots of different ways of achieving the same thing. Documentation helps others to understand how you chose to do it, and why you chose that way. Someone can probably work it out from looking at the code, but that's a lot of work! It's much easier for the original author to write down their thinking and decisions. Remember that the person maintaining your code may in fact be you in the future! If you spend 6 months working on a different project, and then come back to do some bug fixes on a piece of code, almost certainly you'll have forgotten a lot of details on why things were done the way they were. Future you will thank you for having some good documentation. 



Quality management
~~~~~~~~~~~~~~~~~~
Generally, all of the above steps will be wrapped in a *Quality Management Framework*. That is, you'll have a process for testing your code. You'll have a process for checking the security of your code. You'll have a process for capturing the requirements. A quality management system gets you to write down what each of these processes is, and how you sign off that they've been done. The quality management approach is thus a wrapper around the documentation you put in place to support the software lifecycle. 

There are international standards for how to implement quality management, mainly:

- ISO 9001 for general systems.
- ISO 13485 for medical devices.

For safety critical applications, independent auditors will look at your quality control processes, that they're up to standard, and that you've followed them, before letting you sell your software. Even for less critical applications, it's often beneficial to be certified against ISO 9001 to show that good attention to quality is present. This will make customers more likely to choose you. 

A focus on quality and signing off that parts have been tested appropriately won't mean that your software is bug free. That's not a realistic expectation for any non-trivial project. It will, help ensure that the impact of any residual bugs is small. Moreover, if something goes wrong, the documentation helps you identify what went wrong and why. You can then change the quality management process so that similar issues are captured in the future and won't happen again. This continuous improvement is particularly important for shipping high quality products that customers want to buy and trust. 



Software development tools
--------------------------


Comments
~~~~~~~~
Comments allow you to add non-executable information into your .c file. Generally they are used for explaining what the code is doing and why, to keep track of what this unit of code is for, and to explain anything which might not be obvious. Sometimes they are used to deactivate code that you have written, but don't want to be part of the program at the moment (for whatever reason).

Comments aren't a substitute for good documentation, as they can only be text (no diagrams or similar) and they sit at a particular place in your code and so generally explain what's happening only there, rather than giving the big picture. Nevertheless, comments are an essential part of any code.

In C there are two ways of adding comments:
* will start a comment for the rest of the line. Anything after this will be ignored by the compiler and will be for your information only.
* Text inside a block starting with and ending with will be a comment. This lets you add lots of text, without having to start every line with a comment command. 

Examples of C comments might be:



Documentation generators
~~~~~~~~~~~~~~~~~~~~~~~~
We noted previously that comments in the code aren't a substitute for good documentation. Generally comments are quite low level, giving details on exactly what that piece of code is aiming to do and any hints needed to understand complicated operations. In contract, documentation is generally higher level, explaining the overall architecture and design choices made, and explaining how a user should interact with the program to use it correctly. 

You can just write documentation in a word processor such as Microsoft Word or Google Docs and store the file(s) together with the source code for your program. Alternatively, there are lots of dedicated tools available to help you write and maintain the documentation. These dedicated tools more closely link the code and the documentation and so can provide additional features, such as the ability run tests on any examples given the documentation. This is very helpful to ensure the examples are correct! Using dedicated documentation tools can also help to keep the code and its documentation synchronised as updates are applied to the code. 

As one example, Sphinx takes documentation written as text and converts it to be an interactive website which can include code examples and other features. It is used in website such as Read the Docs which is commonly used to share documentation for open source programs. 

Alternatively, DOxygen takes comments in the code file and converts them to be a website, which can include text and code, and have hyperlinks to move between different functions. This has the advantage that there isn't a separate documentation file to maintain, everything (code and documentation) is in the one file. (Which then has the disadvantage of this one place potentially being a messy mixture of code and documentation, which may make it harder to see the underlying code and where the important bits are.)

The different tools available each have their own syntax and detailed methods of using them. As we're only looking at introductory, short, programs we won't use documentation tools in this course. Comments in our code will suffice for now. As you start to move to bigger programs you may like to explore some of the tools listed above (and others you find online, there are many alternatives). 

In general, many documentation tools support the syntax of using three forward slashes (rather than the two used in a normal comment) to indicate this is a piece of documentation to be put on the website, rather than a comment on the underlying code. For example, you might see code like: