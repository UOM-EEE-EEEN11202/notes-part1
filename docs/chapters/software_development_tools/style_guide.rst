.. role:: console(code)
   :language: console

.. role:: c(code)
   :language: c

.. _our_style_guide:

Our code style guide
--------------------
For writing our materials we will use our own style, broadly following conventions common. In particular:

- Filenames will be in *snake case*. That is, all lower case with underscores :console:`_` rather than spaces. Example: :console:`file_name.py`. This is to help avoid cases like :console:`"file name.py"` being accidentally interpreted as two files, one called :console:`"file"` and one called :console:`"name.py"`. (Nevertheless, our code should use delimiters to mark the start and end of a filename to avoid this issue, because in general you can't guarantee what a filename will be.)

- Folders will be in *kebab case*. That is, all lower case with hyphens :console:`-` rather than spaces. Example: :console:`lab-a`. This is to help avoid issues with spaces in folder names, which can cause problems in some command line tools. (This is actually a fairly recent change to our style guide. You might still see some screenshots which use our older style, which used snake case for folders.)

- Variables will be in snake case. Example: :console:`my_variable_name`. Usually, but not always, programming is case sensitive, and so sticking with this helps ensure we don't have :console:`My_variable` and :console:`my_variable`, which are actually two different variables.

- Classes will be in *Pascal case*. That is, all lower case, with uppercase at the start of a new word, with no spaces present. Example: :console:`MyClassName`. 

- Constants will be in capitals. Example: :console:`MY_CONSTANT`.

- We won't use camel case. (Example: :console:`myVariableName`.)

- Code will be indented each time we move into a function, or into an if or while statement, or similar.

- An indent is 4 spaces, entered with the space bar. We won't use tabs for indenting. (This is because different computers may display tabs as having different widths, whereas a space is more fixed.)

- Comments on the same line as code start with a lower case letter, as if they were continuing on a sentence. Comments on a line by-themselves start with an upper case letter, as if they are starting a new sentence. Comments

- Comments have no fixed length before starting a new line. Word wrap in the text editor is used to spread long comments over multiple lines.

- We don't use block comments, :c:`/*` and :c:`*/` to mark a whole section of a file as being comments. 

- Pointers :c:`*` are right aligned. That is, :c:`int *my_pointer;` rather than :c:`int* my_pointer;`. 

