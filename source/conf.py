# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'notes-part1'
copyright = 'Alex Casson. <a class="nav-link text-light" href="https://creativecommons.org/licenses/by/4.0/deed.en">Released under CC-BY 4.0 license.</a>'
author = 'Alex Casson'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme_path = ['./_theme']
html_theme = 'uom_sphinx_wagtail_theme'
html_static_path = ['_static']
html_theme_options = dict(
    project_name = "Notes part 1",
    logo = "/images/uom_logo_white.png",
    logo_alt = "University of Manchester logo",
    logo_url = "/",
    logo_width = 88,
    footer_links = ",".join([
        "The University of Manchester|https://www.manchester.ac.uk/",
        "Canvas|https://online.manchester.ac.uk/",
    ]),
    github_url = "https://github.com/UOM-EEE-EEEN1XXX2/notes-part1",
)
html_favicon = "_static/images/favicon.ico"
html_show_copyright = True
html_css_files = ["uom_custom.css"]
html_sidebars = {"**": [
    "searchbox.html",
    "globaltoc.html",
    "uom_logo_sidebar.html",
]}
html_show_sphinx = False