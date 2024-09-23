project = 'reStructuredText Guide'
copyright = '2024, Carlos Alberto Ramos López'
author = 'Carlos Alberto Ramos López'

release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosummary',
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'venv',
    'Lib',
]

# -- Options for HTML output -------------------------------------------------

html_title = "reStructuredText Guide"
html_theme = "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = [
#     '_static',
# ]

html_theme_options = {
    "show_navbar_depth": 2,
    "max_navbar_depth": 2,
}


latex_elements = {
    'sphinxsetup': '''
        hmargin={0.625in,0.500in},
        vmargin={0.375in,0.750in},
        verbatimwithframe=false
    ''',
    'passoptionstopackages': r'''
    \PassOptionsToPackage{
        paperwidth=6in,
        paperheight=9in,
    }{geometry}
    \PassOptionsToPackage{svgnames}{xcolor}
    ''',
    'preamble': r'\input{preamble.tex.txt}',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'extrapackages': r'''
        \usepackage{changepage}                     % Adjust cover margins.
        \usepackage{enumitem}                       % Remove separation in lists.
        \usepackage{setspace}                       % Modify space between lines.
        \usepackage[final]{microtype}               % Improve typography.
        \usepackage{mathpazo}                       % Change base and math fonts.
        \usepackage[ttdefault=true]{AnonymousPro}   % Changed monospace font.
        \usepackage{calc}                           % To use calculated expressions
        \usepackage{etoolbox}                       % To add content before or after a given environment.
        \usepackage[labelformat=empty]{caption}     % Prevents the "Figure #" text.
    ''',
    'maketitle': r'''
        \input{cover.tex.txt}
        \input{title_page.tex.txt}
        \input{copyright.tex.txt}
        \input{dedication.tex.txt}
    ''',
}

latex_additional_files = [
    'preamble.tex.txt',
    'cover.tex.txt',
    'title_page.tex.txt',
    'copyright.tex.txt',
    'dedication.tex.txt',
    # Images
    'img/LeanPub.pdf',
    'img/LeanPub.png',
    'img/LeanPubW.png',
    'img/CC-BY-NC-SA.png'
]
