Continuous integration
======================

Continuous integration comes when we combine our :ref:`version control system <version_control>` with :ref:`automated testing approaches <automated_testing>`.

You can configure tools to automatically run your test harness whenever you commit your code. It will thus automatically give you a list of what's not working so you know where attention is still required. 

You can go so far as having Git reject any commits which don't pass the tests present. This will ensure that you always have code that works in your repository, and you can't ship code with known issues unless you override this. (Although this might get in the way of good version control of minor changes.)

Common tools include `GitHub Actions <https://github.com/features/actions>`_ and `Jenkins <https://www.jenkins.io/>`_, but there are many others.

.. admonition:: This course

    We won't make use of continuous integration in this course. You don't need to know anything more than what's in these brief notes, unless you want to go further for your own purposes.

    We don't make use of fully continuous integration when making the course materials, but if interested you can view the `GitHub Actions for these notes <https://github.com/UOM-EEE-EEEN1XXX2/notes-part1/tree/main/.github>`_. GitHub Actions automatically update the dependencies for us, and re-build the lecture notes and automatically update the website each time a new version is checked into the Git remote repository. 
