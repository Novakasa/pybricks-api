#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pybricks documentation build configuration file, created by
# sphinx-quickstart on Thu Sep  6 15:31:12 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from sphinx.domains.python import PyClassmember
sys.path.insert(0, os.path.abspath('../..'))

from pybricks import _version  # noqa E402

# ON_RTD is whether we are on readthedocs.org
# this line of code grabbed from docs.readthedocs.org
ON_RTD = os.environ.get('READTHEDOCS', None) == 'True'

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../common/_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'pybricks-micropython'
copyright = '2018-2019 The Pybricks MicroPython Authors'
author = ''

_TITLE = 'Pybricks Modules and Examples'
_DISCLAIMER = 'LEGO, the LEGO logo, MINDSTORMS and the MINDSTORMS EV3 logo are\
               trademarks and/or copyrights of the LEGO Group.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = _version.get_versions()['version']
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Figure numbering
numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s'
}

# -- Autodoc options ------------------------------------------------------

autodoc_member_order = 'bysource'
autodoc_default_flags = ['members', 'undoc-members']
autoclass_content = 'both'  # This ensures init arguments are not ignored
add_module_names = False  # Hide module name

# -- Options for HTML output ----------------------------------------------

if ON_RTD:
    html_theme = 'default'
    html_context = {
        'css_files': [
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/css/theme_overrides.css',
        ],
        'disclaimer': _DISCLAIMER,
    }
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_context = {
        'css_files': [
            '_static/css/theme_overrides.css',
        ],
        'disclaimer': _DISCLAIMER,
    }

html_logo = '../common/images/pybricks-logo-small.png'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
   'style_external_links': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../common/_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pybricksdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
    \makeatletter
    \fancypagestyle{normal}{
        \fancyhf{}
        \fancyfoot[R]{{\py@HeaderFamily\thepage}}
        \fancyfoot[C]{\raisebox{-7mm}{\tiny %(disclaimer)s}}
        \fancyhead[L]{{\py@HeaderFamily \@title}}
        \fancyhead[R]{{\py@HeaderFamily \py@release}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
    }
    \fancypagestyle{plain}{
        \fancyhf{}
        \fancyfoot[R]{{\py@HeaderFamily\thepage}}
        \fancyfoot[C]{\raisebox{-7mm}{\tiny %(disclaimer)s}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
    }
    \makeatother
    ''' % {
        'disclaimer': ' '.join((_DISCLAIMER, '©', copyright)),
    },

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'extraclassoptions': 'openany,oneside',

    'releasename': 'Version',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, ''.join([project, '-v', version, '.tex']), _TITLE,
     author, 'manual'),
]

latex_logo = '../common/images/pybricks-logo-large.png'


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pybricks', 'Pybricks Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Pybricks', 'Pybricks Documentation',
     author, 'Pybricks', 'One line description of project.',
     'Miscellaneous'),
]


def get_signature_prefix_none(self, sig):
    return ''


PyClassmember.get_signature_prefix = get_signature_prefix_none
