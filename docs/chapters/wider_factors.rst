.. role:: python(code)
   :language: python

Wider factors to consider
=========================

As with most beginning programming courses, most of this course will focus on writing code to achieve a specific function. Getting code that has the correct functionality, without bugs or other issues, is the core goal. There's plenty to learn just doing this!

Of course, for high quality code there are lots of other factors that need to be taken into account, beyond only *does the code implement the correct function*. We discuss some of these briefly here.


Security and risk
-----------------
Cyber security and the hacking of computer systems are major concerns for many organizations which handle sensitive data. Which is basically every organization, no one wants their private data to be stolen.

In the UK, there are laws which govern how some information has to be kept securely. If data is stolen, it has to be reported to the `Information Commissioner's Office <https://ico.org.uk/>`_, and potentially there can be fines and other sanctions if suitable procedures are not followed. Organizations routinely rate cyber attacks as one of the highest impact, and most probable, risks that they face and have to take actions to mitigate against. 

Poor programming can give many attack vectors for hackers and other malicious actors to exploit. For the small projects we consider in this course, attacks on the code likely won't be a major concern, but they may be a substantial design constraint in bigger real-world projects. 

When discussing :ref:`using code from the Internet <code_security>` we already highlighted that you should take care when downloading and running external code. A key :ref:`motivation <motivation>` for our focus on Rust, with a smaller portion of C/C++, is to set you on a path to producing code with fewer memory safety issues which could lead to security vulnerabilities. 


Sustainability
--------------
Environmental and financial sustainability is very important. All of our computers use power, and if our programs are inefficient, they will use more power and more resources than they need to. In the scheme of things, each individual computer only consumes a small amount of power. This adds up though! 

It is estimated that about `10% of the world's electricity is used on Information and Communications Technologies <https://doi-org.manchester.idm.oclc.org/10.1145/3613207>`_. Each query on ChatGPT is (roughly) equivalent to `keeping a light on for 5 minutes <https://medium.com/@zodhyatech/how-much-energy-does-chatgpt-consume-4cba1a7aef85>`_. Data centres also use a lot of water for cooling. In addition to the environmental impact, electricity costs money, as does cooling to manage the temperature of computers. 

There's then the electronic waste impact. Code which can run using only very few resources will likely be able to run on older harder, keeping it in service for longer and reducing how much we have to throw away. In programming there's often more than one way to achieve the same function. We'll touch briefly on computational complexity, but for big projects you might need to dig deeper and look at how to optimize the run time, or other resource requirements, of your code with an eye on the sustainability impact. 

In 2015, UN member states agreed to 17 global Sustainable Development Goals (SDGs) to end poverty, protect the planet, and ensure prosperity for all. Being a fundamental technology with many applications, there are likely examples of computer programs which contribute towards all 17 goals. 

For example, code to analyze medical data and produce a summary report might contribute to *Goal 3: Good health and wellbeing*. Code monitoring the amount of renewable energy being generated, and changing how this is passed to the grid, might contribute to *Goal 7: Affordable and clean energy*. Code modelling water flows and leakages in water pipes might contribute to *Goal 6: Clean water and sanitation.* There are many more possible examples. 


Equality, Diversity, Inclusion and Accessibility
------------------------------------------------
Essentially, everybody uses and needs access to computers and the results of computer code. Equality, diversity, inclusion and accessibility are thus important to consider, and there are many places where they interact with the code that we write. We'll briefly list a few examples below, but there are many more.

Our code is fundamentally written in English. Commands such as :python:`print` to display something to the screen, assume familiarity with written English. We've discussed :ref:`text encoding <text_encoding>` previously. While modern code and programs will nearly all support UTF-8 and having non-English characters, for example with accents and similar, it's not super-uncommon to still run into programs that struggle with non-ASCII characters.

In our programs, needing to store a person's name is fairly common. Here's an example list of `falsehoods programmers believe about names <https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/>`_. Without care and thought, and inclusive co-design, it's easy to accidentally make code that some people can't put their name into.

We're going to use Git a lot for our version control. We noted that Git can have *branches*, allowing multiple copies of the same code to be developed in parallel. Today the default branch is called *main*. Historically it was called *master*. The implication being that there were slave branches.

We've tried to make these notes as inclusive and as accessible as possible. They have a dark mode, and a mode using a Dyslexia accessible font. Many of the tools we're going to use, such as VSCode, are very customizable. They can be set up to use colors, contrasts, and fonts that the user prefers. It is generally up to the user to change the default settings though. 
