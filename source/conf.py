# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys, os
import glob
import rst2pdf

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.dirname(__file__))


# -- Project information -----------------------------------------------------

project = 'Wiki Network Engineering Mirror'
copyright = 'Transcriber Mentality'
author = 'Richelin Metellus'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
try:
    version = open(os.path.join(project_root, 'VERSION'), 'r').read().rstrip()
    release = version
except:
   version = '0.1'
   release = '0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# myst_parser for markdown with sphinx - pip install  --upgrade myst-parser
extensions = [
    'sphinx.ext.autodoc',
    'myst_parser',
    'rst2pdf.pdfbuilder',
    'sphinx-prompt', 
    'sphinx_substitution_extensions',
    'sphinxcontrib.drawio',
    'sphinx_tabs.tabs',
    'sphinx_toolbox.collapse',
    'sphinxcontrib.plantuml',
    'sphinx_design'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.rst.inc': 'restructuredtext',
    '.md': 'markdown',
}

### Setup for plantuml
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
else:
    # need to add the path in the form [ "string", "string", ...] for quoted path.
    plantuml = ["java", "-jar", os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "_tools", "plantuml.jar"))]
    print("plantuml path:", plantuml)
    plantuml_output_format = 'png'

autoclass_content = 'both'

# This extend the markdown CommonMark specification
# This enable all extension which is off by default
myst_enable_extensions = [
    # "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']
pygments_style = 'sphinx'


# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# import sphinx_rtd_theme
html_theme = 'cloud'
# Modify the cloud.css theme to match your prefer styling by
# modifying individual css element.
html_style = ['CloudThemeOverride.css', 'rcky-customStyle.css']
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Blob style doesn't work for this one.
# A list of paths that contain extra files not directly related to the documentation, such as 
# robots.txt or .htaccess. Relative paths are taken as relative to the configuration directory. 
# They are copied to the output directory. They will overwrite any existing file of the same name.
html_extra_path = []

# html_file_suffix = ".aspx" # change in order to view on sharepoint
# -- Options for PDF output -------------------------------------------------

pdf_language = 'en_US'

pdf_fit_mode = 'shrink'
pdf_break_level = 1
pdf_breakside = 'any'
pdf_cover_template = 'sphinxcover.tmpl'
pdf_invariant = False
pdf_use_toc = True
pdf_toc_depth = 9999
# Background images fitting mode
pdf_fit_background_mode = 'scale'

pdf_use_index = False
pdf_use_modindex = False

pdf_stylesheets = ['sphinx', 'letter']
pdf_documents = [ 

]