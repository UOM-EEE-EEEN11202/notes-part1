Software lifecycle
==================

The software lifecycle refers to us considering all of the steps involved in writing, deploying, and maintaining code. There are international standards that set out the steps that people/teams/organisations should go through:

- ISO/IEC/IEEE 12207 covers general software.
- IEC 62304 covers medical device software. 

Generally, the higher risk the software (e.g. for medical devices, for planes vs. for toasters, for TVs) the more steps, documentation, and testing are required. 

We won't go through these international standards in detail, but will briefly overview the steps in the following sections. Some will come across as common sense, but as the saying goes, "common sense isn't always that common". It's easy to skip some steps, or to do them too briefly, and build up problems that make the code hard to maintain.

.. toctree::
   :maxdepth: 2
   :hidden:

   software_lifecycle/requirements_capture
   software_lifecycle/software_architecture
   software_lifecycle/testing_and_debugging
   software_lifecycle/release
   software_lifecycle/documentation
   software_lifecycle/quality_management