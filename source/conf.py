# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphnx-link-by-labels-ext'
copyright = '2023, Sviatoslav Sydorenko <webknjaz@redhat.com>'
author = 'Sviatoslav Sydorenko <webknjaz@redhat.com>'

version = '1.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys; sys.path.insert(0, f'{__file__.rsplit("/", 1)[0]}/_ext')
extensions = ['sphnx_link_by_labels.ext']

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
