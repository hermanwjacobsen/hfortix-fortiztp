# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'HFortix-FortiZTP'
copyright = '2026, Herman W. Jacobsen'
author = 'Herman W. Jacobsen'

# The full version, including alpha/beta/rc tags
try:
    from hfortix_fortiztp import __version__
    release = __version__
    version = '.'.join(__version__.split('.')[:2])
except ImportError:
    release = '0.5.163'
    version = '0.5'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

templates_path: list[str] = ['_templates']
exclude_patterns: list[str] = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path: list[str] = ['_static']

# -- Extension configuration -------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'hfortix_core': ('https://hfortix-core.readthedocs.io/en/latest/', None),
}
