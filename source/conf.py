# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'notes-part1'
copyright = '2024, Alex Casson'
author = 'Alex Casson'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en-GB'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
html_theme_options = dict(
    project_name = "Notes part 1",
    logo = "/images/uom_logo.png",
    logo_alt = "University of Manchester logo",
    logo_height = 109,
    logo_url = "/",
    logo_width = 46,
    footer_links = ",".join([
        "The University of Manchester|https://www.manchester.ac.uk/",
        "Canvas|https://online.manchester.ac.uk/",
    ]),
)
html_favicon = "_static/images/favicon.ico"
html_show_copyright = True
html_css_files = ["custom.css"]
html_sidebars = {"**": [
    "searchbox.html",
    "globaltoc.html",
    "custom_sidebar.html",    # Your template here
]}