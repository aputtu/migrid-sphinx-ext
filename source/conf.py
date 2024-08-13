# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys


# -- Path setup for custom extensions ---------------------------------------
sys.path.insert(0, os.path.abspath('extensions'))


# -- Project information ----------------------------------------------------
project = 'migrid-sphinx-ext'
# noinspection PyShadowingBuiltins
copyright = '2024, Aputsiak Niels Janussen'
author = 'Aputsiak Niels Janussen'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'accordion.accordion',
    'lightbox.lightbox',
]

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_static_path = [
    '_static',
    'extensions/accordion/static',
    'extensions/lightbox/static',
    'img',
]


html_lightbox_image_path = '_static'

# -- Options for LaTeX output ------------------------------------------------

# Needed for accordion extension, very experimemtal stage
# Not tested on lightbox extension yet
latex_elements = {
    'preamble': r'''
    \newenvironment{details}{\par\smallskip\noindent}{\par}
    \newcommand{\detailssummary}[1]{\textbf{#1}\par}
    ''',
    'extraclassoptions': 'openany,oneside'
}



