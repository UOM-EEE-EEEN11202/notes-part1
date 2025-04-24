.. role:: console(code)
   :language: console

Environment control
===================

Version control is for keeping track of the code and documentation files that we make, letting us roll back to previous versions or see changes from previous versions. 

Often there might be a wide range of other files or information that are needed to make your code work, beyond the main code files themselves. In particular, there is the *version* of the programming language and tools (IDE, operating system, etc.) that you use. 

Python has lots of different versions (e.g. 3.7, 3.10, 3.13), changing as new features are added. A new version is released each year, which then has active support for 2 years, and security support for 5 years. Rust is released in *editions* every 3 years and also has versions released more frequently. We'll also find it's common to load external code as part of a Python or Rust program. Each one of these *modules* or *libraries* will also have a version, which changes over time. 

Environment control helps us lock the development environment, ensuring that you're using a fixed, known set of versions for everything. If there are multiple people all working on the same project, environment control also helps ensure everyone is using the same versions. 

Environment control software gives us tools for keeping track of which versions of the different tools and libraries are installed, and potentially to have multiple versions of these installed at the same time so we can move to different versions as required. They make a *container*, or a *virtual environment*, or possibly a complete virtual computer (a virtual machine) inside your real computer. You can have multiple containers running at the same time, each with different development environments installed in them. 

There are several parts to environment control:

#. There is a *container* which defines the operating system to be used and the programs it should have installed. `Docker <https://www.docker.com/>`_,  `Podman <https://podman.io/>`_ and `kubernetes <https://kubernetes.io/>`_ are popular choices. (Generally Docker is the starting point, and kubernetes is for larger cloud based projects.) The user of the container may or may not be allowed to install additional programs.

#. There is a *devcontainer* which configures the development environment, VSCode in our case, to have the settings we want. For VSCode, this is mainly installing the extensions needed for the different programming languages to be used. 

#. (Python only.) There is a *virtual environment* which defines the specific version of Python and the various modules being used. You may have multiple virtual environments if you have code that needs different versions of Python to run. Typically we have one virtual environment per *project*, and it's up to the user to define how big or small each project is. Generally it's bad practice to just have one global virtual environment for all of your work. You'll probably quickly find you have conflicts in which versions of modules are needed in order for different parts of the code to work. 

#. There is a *configuration file* setting up the project, listing its *dependencies*. That is, what version of the programming language is being used; and whether there are any external modules that are being used to add functionality, and if so whether there are any constraints on which versions can be used. In Python, there are a number of options, but these would generally be listed in a :console:`pyproject.toml` file (or a :console:`requirements.txt` file in older projects). In Rust, the configuration is kept in a :console:`Cargo.toml` file. 

.. admonition:: This course

    We don't expect you to know about containers and devcontainers. We have made these for you (because we want everyone to be using the same versions of the different tools needed!). You just need to follow the instructions given in the lab notes. Once you have a programming environment setup, you probably won't need to refer to these pages again. If you're interested, our *dockerfile* which defines the EEEN11202 container is in our `GitHub repository <https://github.com/UOM-EEE-EEEN1XXX2/dockerfile>`_, as is our `devcontainer file  <https://github.com/UOM-EEE-EEEN1XXX2/devcontainer>`_.

    For Python, we do expect you to know about, and be able to use, virtual environments. They are an essential part of knowing Python, and we'll use them throughout the labs. 

    We'll also make use of :console:`pyproject.toml` and :console:`Cargo.toml` files where appropriate. We'd expect you to have some knowledge of these, only to the extent that we use them in the labs. 
