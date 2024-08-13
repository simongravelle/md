# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'get-help'
copyright = '2024, Simon Gravelle'
author = 'Simon Gravelle'
release = '0.0.1'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_title = "    "

html_static_path = ['_static']

pygments_style = 'tango'

source_suffix = ['.rst']