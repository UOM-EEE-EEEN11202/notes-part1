.. role:: python(code)
   :language: python

.. role:: console(code)
   :language: console

.. role:: rust(code)
   :language: rust

Error handling (asserts and exceptions)
=======================================

Assert statements
-----------------
We've discussed automated testing (unit and integration testing) :ref:`previously <automated_testing>` but didn't go into how these are actually carried out.

The basic building block for automated testing is an *assert* statement. This might look something like

.. code-block:: python

    assert x == 0

This assert statement means *at this point I the programmer know x should be 0. If it is, carry on as usual. If it's not, flag that the test has failed*. 

There are lots of different types of assert checks that can be use. Generally they rely on you the programmer having some knowledge (for your given test input) of what the code should ideally be doing at a particular point. 

Assert statements are for you the programmer, letting you test the code. They are not intended for displaying errors to users. It's possible, for example, to automatically turn assert statements off. That is, they are still in the code, the code remains unedited, but they are just ignored when the code runs. They thus don't have any performance impact. It's possible to run code in *debug* mode, or in *deployment mode* by changing some settings which change how much optimization is performed behind the scenes.

If you run a Python program :python:`my_script.py` from the command line, rather than using a GUI, usually you would start it with

.. code-block:: console
   
   > python3 my_script.py

If you add the optional :console:`-O`, all debug and assert statements will be ignored, probably making the code run faster.

.. code-block:: console
   
   > python3 -O my_script.py

Adding :console:`-OO` will perform even more optimizations.


Exceptions
----------
For displaying errors to users *exceptions* are used (or their equivalent - not all languages use the same term or approach here). 

You can *raise* an exception directly, for example as:

.. code-block:: python

    print("Enter a number larger than 0")
    inp = input()  # pauses and gets input from the keyboard
    inp_int = int(inp)  # converts the input to an integer

    if inp_int <= 0:
        raise Exception("Error! The number you entered was less than 0.")

Here it's very directly an error by the user that's being checked, and so this is handled via an exception. This will present an error message to the user, in red, and you can add information to help the reader understand what went wrong. 

Commonly the above Python syntax isn't used directly. *try-except* (also known as *try-catch*) blocks are used. These *try* to do the commands given, and if they don't work raise the following error. An example is:

.. code-block:: python

    fn = "file.txt"
    try:
        # If file fn already exits, open it in 'append' mode. That this, to add text on at the end of the existing file
        with open(fn, "a") as f:
            f.write("Hello")
    except FileNotFoundError:
        # If an error occurs, make a new file and write in this blank file
        with open(fn, "w") as f:
            f.write("world")

The above is an example of a *recoverable* error. If the file to use doesn't exist, it switches to making a new file instead. You can also have *unrecoverable* errors, where it's not meaningful for the program to keep going. Here the program just needs to stop (first closing any open files, or network connections, or similar) and then pass an error message to the user.  

Rust separates between *recoverable* and *unrecoverable* errors more than Python does. It has a dedicated error handling data type :rust:`Result<T, E>`. This gives an object, which contains the successful output, :rust:`T` here; and any errors produced, called :rust:`E` here. You can then check whether the result was :rust:`Ok` in which case you perform one action, or whether the result contained an error, in which case you carry out a different action. For example:

.. code-block:: rust

   let file_result = File::open("file.txt");

   let file = match file_result {
       Ok(file) => file,
       Err(error) => panic!("Problem opening the file: {error:?}"),
    };

Here the aim is to set :rust:`file` to be the opened :rust:`"file.txt"`. Rather than just doing this in a single line of code, to allow us to check for errors (such as the file not existing) :rust:`File::open("file.txt")` returns a :rust:`Result<>` data type into an intermediate variable called :rust:`file_result`. There is then a :rust:`match` function. If the contents of :rust:`file_result` indicate the operation worked, :rust:`Ok()`, :rust:`file` is set as was wanted. If they indicate that an error occurred, :rust:`Err()`, :rust:`panic!()` is called. :rust:`panic!()` causes the program to terminate, and in this case display an error message. More generally this gives you a place for any *error handling code* to determine what to do if an error occurs.

It's up to you as the program designer to decide how much error handling you want to do. This is an important part of the overall program design - we can't assume that actions are always successful, particularly when they involve interacting with the outside world. We may want to open a file, but have the filename wrong. We may want to access a resource on the Internet, but our network connection isn't working. For all of these type of cases you likely want to add some error handling code that the program terminates gracefully rather than just crashing. 

.. admonition:: This course

    We'll see examples of using this functionality in the labs, particularly when we look at testing. 