.. Accordion extension with accessibility baked in documentation master file, created by
   sphinx-quickstart on Sat Aug  3 23:08:31 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Extensions for MiGrid user documentation
========================================
The MiGrid Sphinx extensions allows for custom directives using the
`Sphinx documentation system <https://sphinx-doc.org>`_.

The aim is to adhere to the most important
`W3C Web Accessibility Initiative (WAI) <https://www.w3.org/WAI/>`_,
even for browsers not supporting JavaScript.

The code is licensed under a
`free and open source software license <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.

Status
^^^^^^

The current release is 0.1.0. It has been tested with sphinx-build 7.2.6 and Python 3.10.12.
The extension is available on `Github <https://github.com/aputtu/migrid-sphinx-ext>`_.

.. accordion:: Lightbox TODOs/Ideas list

   - [x] Lightbox image works
   - [x] Lightbox image has optional caption
   - [x] Lightbox image has optional percentage
   - [x] Lightbox image can be closed by clicking on image or close button
   - [x] Fix: Scale image background to image in both width and height for lightbox.
   - [ ] Look into if white background-color can be avoided or is set for wrong element.
   - [ ] Consider whether close button should always be visible
   - [ ] Fix: A form control has more than one label associated with it.
   - [ ] Fix: Contrast on code blocks is insufficient according to WCAG 2.0 AA contrast ratio.
   - [ ] Allow for aligning images to left, center or right in normal state etc.

.. accordion:: Accordion TODOs/Ideas list

   - [x] Nesting of accordions
   - [ ] Improve styling of accordion header, especially for differentiating main accordions
   - [ ] Format for nicer PDF output ("make latexpdf" runs)
   - [ ] Optional JavaScript for expanding/collapsing multiple accordions with one click

.. accordion:: Common TODOs/Ideas list for extensions

   - [x] Move configuration from conf.py into extesnsion where possible
   - [ ] Simplify configuration and installation process (pip install or similar)
   - [ ] Verify that it works on multiple browsers / screen readers
   - [ ] Telling error messages when parsing of rst files fails
   - [ ] Look into whether extension works with .md files
   - [ ] Improve robustness of extension; flake8, pylint, unit tests, etc.

|

Extension: Lightbox
===================
The extension  :code:`lightbox` is a simple extension, that allows for an image
to be displayed in two states: normal and lightbox mode.

In lightbox mode an optional text caption can be displayed.

Usage instructions
^^^^^^^^^^^^^^^^^^
Example of using lightbox directive with all available options:

.. code-block::

   .. lightbox:: img/gnu.webp
       :alt: GNU logo
       :caption: The GNU logo
       :percentage: 30 95

Outputs:

.. lightbox:: img/gnu.webp
    :alt: GNU logo
    :caption: The GNU logo
    :percentage: 30 95


Options
^^^^^^^
Using the options is recommended, but not required.

#. Option :code:`:alt:` is the alternative text.
#. Option :code:`:caption:` is the caption text, shown below image in lightbox mode.
#. Option :code:`:percentage:` allows for two numerical values. If used, first value is mandatory. Examples:

   #. Using :code:`:percentage: 30` shows 30% of the container width in normal state.
   #. Using :code:`:percentage: 30 95` shows 30% of the container width in normal state, and 95% in lightbox state.

The image widths for normal and lightbox state defaults to 100% of its parent container width,
if :code:`:percentage:` is left out.

When lightbox state is active, clicking anywhere on the image will close the lightbox.
There is also a close button indicator in the top right corner, but it is only visible when second value of
:code:`:percentage:` is set to less than 100; like :code:`:percentage: 30 95`

|

Extension: Accordion
====================

The extension  :code:`accordion` is a simple extension, that allows for accordions.
Accordions are simply content containers be expanded and collapsed. This allows for
hiding content that may not be immediately relevant to the general user.

Examples when you may want to hide information:

*  You may want to provide usage instructions that vary on different operating systems.
   Here an accordion per operating system can hide irrelevant content.
*  You may want to provide a list of links to other resources.
*  Your main content provide general instructions, the accordions show advanced instructions.


Key technical features
^^^^^^^^^^^^^^^^^^^^^^^

The main feature is ease of use, both for the author and the user.

* Only CSS is used, no JavaScript.
* Author can continue to use reStructuredText and nest accordions intutively.
* Accessibility: keyboard navigation, screen readers, etc.
* The extension is easy to install and configure.

Usage instructions
^^^^^^^^^^^^^^^^^^^^

The extension is used when you add directives to your reStructuredText files.
The following example shows what is possible with the extension.
You can use the "View page source" to see the reStructuredText code.

==========================
Default is collapsed state
==========================

.. accordion:: Accordion element collapsed by default.

   .. accordion:: Accordion inside another. Set with option :expand:
       :expand:

       Yet another accordion in expanded state.

   .. accordion:: Plain accordion. Collapsed state is the default

       Yet another accordion. Yihaa!



   You can insert accordions inside accordions, and they work just fine.
   But you probably want to adjust styling at some point.


==================================
Expanded state set as the default
==================================

.. accordion:: Accordion element with option: :expand:
   :expand:

   Use of *italics* and **bolding** is possible.

   You can also use :emphasis:`emphasis` and :strong:`strong`.

   Other options are: :subscript:`subscript`, :superscript:`superscript`, :title-reference:`title-reference`.

   You can insert, say :code:`.. code-block:: html` inside accordions, and it displays code:

   .. code-block:: html

      <div class="accordion">
         <div class="accordion-header">
            <h3>Example of HTML code inside accordion.</h3>
         </div>
      <div class="accordion-content">


   As you can see above, you can insert accordions inside accordions, and they work just fine.
   But you probably want to adjust styling at some point.


|


Installation instructions
=========================

In order to install the extension, you need to clone the repository to your local machine.
No pip install or similar is available at this time.

Modify Sphinx configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Extension installation**
Instruct Sphinx to look for the extension in the :code:`<your-extension>` folder.
The following *assumes* that folder is named :code:`extensions`, anc placed in the root of your project.
(

.. code-block:: text

   sys.path.insert(0, os.path.abspath('extensions'))


Also, make sure to include extension to the list of extensions, like:

.. code-block:: text

   extensions = [
      ... # other extensions
      'accordion',
      'lightbox',
   ]
