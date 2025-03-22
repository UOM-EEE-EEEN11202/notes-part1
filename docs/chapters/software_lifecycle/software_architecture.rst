.. _software_architecture:

Software architecture
=====================

Software architecture refers to how you choose to split up your code and implement the required functionality. You could put everything in one big file, but that probably isn't the best way to do it! Usually we split the code up by function. 

Continuing our example of detecting car number plates, maybe you have one unit of code which identifies where a number plate is in a camera picture, and another unit of code that does letter/number recognition on this. Each part has its own distinct aim, and they can potentially be developed separately (for example by different developers) before being brought together.

There are lots of decisions that need to be made here. How do the two bits of code talk to each other? For the code which identifies where a number plate is, is the output a set of coordinates telling the other function where to look, or is it an image which has been cropped from the main picture to show just the area of interest? Both are potentially fine, you just need to agree which you're doing. 

Defining the architecture of software typically involves:

- Within the overall goal of the program, defining what the main functions are and how these will be grouped together. 
- Defining what the interfaces between these different functions will be. 

For a large problem, this then gives you a high level blueprint to build your more detailed code against. In the same way that you wouldn't start building a house without a reasonably detailed plan of what you're going to build, you shouldn't start writing complicated code without a reasonably detailed plan of what it's going to look like. It helps makes the task more manageable by breaking it down into smaller chunks, and makes it easier to identify where in the code particular functionality is implemented (because you can look it up in the architecture rather than the more detailed code). 

Again, the architecture wants to be written down, so that everybody knows what it is they're trying to build. Design it, and then code it. Not the other way round. (Any architecture will probably be iterated several times during the process of actually writing the code, adding more detail each time, and that's fine.)
