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
html_css_files = ["custom.css"]

pygments_style = 'tango'

source_suffix = ['.rst']

html_show_copyright = False
html_show_sphinx = False
html_short_title = "True"