.. _software_licenses:

Software licenses
=================

In programming, there is a strong tradition of *open source* outputs. Sometimes companies want to keep their code private, or proprietary, so that others can't copy what they've done. Other times, volunteers will freely offer to contribute code to a project to add features that are important to them. If the code is open source, they can do this. 

Moreover, for some code, being open source means that many people can look at it, and help identify bugs or security vulnerabilities. Also, people often like to share their code so that others can re-use it to help them meet their objectives more quickly. This may be altruistic, making a contribution to the community to help others. 

Just because your code is open source doesn't mean that you can't make money from it. Many companies fundamentally work on open source code, and then charge for providing support to users.

If writing open source code, the worst thing you can do is *just stick it on the Internet*. This doesn't give any potential users information on what they need to do to use the code legitimately. What is the author of the code responsible for, vs. the person that uses it in their project? What acknowledgement or recognition needs to be given to the original author? All open code should be accompanied by a *license*, which says what the code can and can't be used for, and any restrictions or requirements for its use. 

If you set up a new repository at (say) `GitHub <https://github.com/>`_, it will ask you what license you want to attach to the code. There are many different licenses you might choose between. Briefly, some major ones:

- MIT license. This is a very permissive license. It basically says you can do what you like with the code, but the original author isn't involved. They hope it's useful, but otherwise it's up to you to make it work. You have to include a copyright statement saying who wrote the code.

- BSD license (3 clause). Is also very permissive, but says you can't advertise the name of the original author as an endorsement of your software. 

- GPL license (version 2 or version 3). Aims to avoid restrictions being placed on software. If you use or modify GPL code, that code will have the same GPL requirements. Thus, if you use GPL licensed code in your project, and you update that code, you are asked to provide the updated code to users. You can sell GPL code, but you then can't limit a user's right to modify or distribute the code.

- CC-BY. The above are licenses for code. For text and documents, CC-BY is a commonly used license. There are a number of variants, generally asking you to give attribution to the original author, and to indicate what changes have been made.

Sites such as `choosealicense <https://choosealicense.com/appendix/>`_ and `creative commons <https://creativecommons.org/share-your-work/cclicenses/>`_ have tools to help you pick a license. 

Depending on the needs of your project or company, the different licenses may mean you can't use some code in your project, even if fundamentally it's publicly available for people to use. You should read the license, and what it lets you do, before using code in a project. 

.. |ico1| image:: GitHub_Invertocat_Dark.svg 
            :width: 20

.. admonition:: This course

   Your code, even on `GitHub <https://github.com/>`_, will be private, and so we won't ask you to add a license. You thus don't need to have any more familiarity than the contents of these notes. After the course, if you start your own programming projects and sharing your code publicly online, you should think about which license to add.

   For the course notes, we use a range of different licenses (after getting permission from the University of Manchester for the core course to be open source). If you click on the GitHub (|ico1|) icon to view the source for the notes, the GitHub site will contain information on the license(s). Usually our code is under an MIT license, and text under a CC-BY license. Where items have been used from others (such as the fonts), a number of different licenses are present. 