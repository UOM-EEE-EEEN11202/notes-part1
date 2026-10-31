# uom_sphinx_wagtail_theme
University of Manchester Sphinx theme. 

This has added University of Manchester branding/colouring. It has also added an alternative font mode, where the text 
is displayed using OpenDyslexic rather than the default Roboto.


## Usage

It is intended to be included as a Git submodule in other Sphinx projects. 

In the same folder as your project's `conf.py`

```console
mkdir -p submodules
cd submodules
git submodule add https://github.com/UOM-EEE-EEEN11202/uom_sphinx_wagtail_theme.git
```

In addition to the extensions you already have, add

```python
extensions = [
    "...",
    "sphinx_wagtail_theme"
]
```

These two directives needed to activate the theme.

```python
html_theme_path = ["submodules"]
html_theme = "uom_sphinx_wagtail_theme"
```


## Devel

The alternative font mode is somewhat hard coded, particularly for the font-name variable. Moreover, the wagtail theme 
doesn't use pygment for code highlighting—it has a fixed static colour scheme. To get the code changing, we thus just 
hard code over this hard coding!

```console
pygmentize -S default -f html -a .highlight > pygments-theme-light.css
pygmentize -S monokai -f html -a .highlight > pygments-theme-dark.css
```

The commands above were used to generate css files. These are then just loaded over the default wagtail pygments.css file. 
Note that the "default" colour scheme doesn't include all of the classes that are in the wagtail pygments.css, and so these 
classes were added in by hand so that our css file takes precedence in every case.

## Acknowledgements

This is a modified version of the [sphinx-wagtail-theme]: https://github.com/wagtail/sphinx-wagtail-theme, 
which is released, modified, and included here under an MIT license. 

OpenDyslexic and OpenDyslexicMono fonts are included from [OpenDyslexic]: https://opendyslexic.org/,  
released and included here under an SIL Open Font License v1.1.
