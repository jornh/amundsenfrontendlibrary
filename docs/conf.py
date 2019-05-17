import sys, os

sys.path.append(os.path.abspath('sphinxext'))


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "recommonmark",
    "sphinx.ext.autosummary",
    "sphinxcontrib.autohttp.flask",
    "sphinxcontrib.autohttp.flaskqref",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# General information about the project.
project = u"Amundsen"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "show_powered_by": False,
    "github_user": "lyft",
    "github_repo": "amundsenfrontendlibrary",
    "github_banner": True,
#    "show_related": False,
    "note_bg": "#FFF59C",
}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False #True

#################

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "../amundsen_application/static/images/favicon.png"