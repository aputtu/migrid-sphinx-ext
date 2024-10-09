Name: MiGrid Sphinx Extensions
------------------------------


This project contains extensions for the Sphinx documentation project.
They are used to create the documentation for the MiGrid project's User Documentation.

What is it?
-----------
Currently it contains a custom sphinx extensions that through CSS only allows for:

* creating accordions
* creating lightbox images

Further information found in [index.rst](source/index.rst).

Installation:
-------------
Running `make dependencies` and `make html` will install dependencies and build the documentation in html.
The documentation  itself is show as a Sphinx project.

More detailed instructions from commandline:

`git clone https://github.com/aputtu/migrid-sphinx-ext.git`

`cd migrid-spinx-ext`

`make dependencies`

`make html`

The `make html` creates the main HTML page in build folder in ../migrid-sphinx-/build/html/index.html

If you have Firefox installed, display main page with:

`firefox build/html/index.html`



Systems requirements:
-------------------
This is an very early release and has not been tested on all systems.

It was built with:
* Python 3.10
* Sphinx-builder 7.2.6 
* Ubuntu 22.04
