# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '可视计算与交互概论'
copyright = '2024, 北京大学可视计算与学习实验室'
author = '北京大学可视计算与学习实验室'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_multitoc_numbering',
    'sphinxcontrib.bibtex'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

numfig = True
numfig_format = {
	'figure': '图 %s',
	'table': '表 %s',
	'code-block': '代码 %s',
	'section': '§%s'
}

# -- Options for Math --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math

# math_number_all = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = '可视计算与交互概论'

## -- Extensions configuration ------------------------------------------------

bibtex_bibfiles = ['reference.bib']

myst_enable_extensions = [
    "dollarmath"
]

myst_dmath_double_inline = True