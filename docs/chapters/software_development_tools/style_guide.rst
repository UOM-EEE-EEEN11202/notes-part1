.. role:: console(code)
   :language: console

.. role:: c(code)
   :language: c

Code style guide
----------------
In general, there are many ways in which you can format or layout your code, all of which will work. That said, how you layout your code can have a big impact on how easy it is to read and to debug.

Most  companies will have an internal style guide for how to structure and format code so that it looks consistent between different developers and is easy for different people to work on the same codebase. In large projects there may be many different people coding different parts of the program. For example, you can view the `Google style guide <https://google.github.io/styleguide/>`_. Python as a language has an official style guide known as `PEP 8 <https://peps.python.org/pep-0008/>`_. Rust also has an official `style guide <https://doc.rust-lang.org/beta/style-guide/index.html/>`_. For C and C++ there are various style guides, including the `Google C++ style guide <https://google.github.io/styleguide/cppguide.html>`_ and the `Linux kernel coding style <https://www.kernel.org/doc/html/v4.10/process/coding-style.html>`_.

There are also automatic tools that you can use to check your code style against a standard, and to automatically convert code between different styles. In our setup of VSCode we automatically turn these on to help with formatting your code. You'll find that your code gets re-formatted by the auto-formatter each time you save it. Beyond this, we don't have a strictly enforced style guide. For assessed parts of the course, you'll receive marks whatever style you use.  
 
For writing these notes, we will use our own style, broadly following conventions common. In particular:

- Filenames will be in *snake case*. That is, all lower case with underscores :console:`_` rather than spaces. Example: :console:`file_name.py`. This is to help avoid cases like :console:`"file name.py"` being accidentally interpreted as two files, one called :console:`"file"` and one called :console:`"name.c"`. (Nevertheless, our code should use delimiters to mark the start and end of a filename to avoid this issue, because in general you can't guarantee what a filename will be.)

- Folders will be in *kebab case*. That is, all lower case with hyphens :console:`-` rather than spaces. Example: :console:`lab-a`. This is to help avoid issues with spaces in folder names, which can cause problems in some command line tools. (This is actually a fairly recent change to our style guide. You might still see some screenshots which use our older style, which used snake case for folders.)

- Variables will be in snake case. Example: :console:`my_variable_name`. Usually, but not always, programming is case sensitive, and so sticking with this helps ensure we don't have :console:`My_variable` and :console:`my_variable`, which are actually two different variables.

- Classes will be in *Pascal case*. That is, all lower case, with uppercase at the start of a new word, with no spaces present. Example: :console:`MyClassName`. 

- Constants will be in capitals. Example: :console:`MY_CONSTANT`.

- We won't use camel case. (Example: :console:`myVariableName`.)

- Code will be indented each time we move into a function, or into an if or while statement, or similar.

- An indent is 2 or 4 spaces, entered with the space bar. We won't use tabs for indenting. (This is because different computers may display tabs as having different widths, whereas a space is more fixed.)

- Comments on the same line as code start with a lower case letter, as if they were continuing on a sentence. Comments on a line by-themselves start with an upper case letter, as if they are starting a new sentence. Comments

- Comments have no fixed length before starting a new line. Word wrap in the text editor is used to spread long comments over multiple lines.

- Pointers :c:`*` are right aligned. That is, :c:`int *my_pointer;` rather than :c:`int* my_pointer;`. 

