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
    'sphinxcontrib.bibtex',
	'sphinx_subfigure',
	'sphinx_proof'
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

# -- Build Options -----------------------------------------------------------

html_favicon = '_static/favicon.png'

# -- Options for Math --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math

# math_number_all = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = '可视计算与交互概论'

## -- Extensions configuration ------------------------------------------------

bibtex_bibfiles = [
	'geometry/reconstruction/ref.bib',
	'geometry/transformation/ref.bib',
	'geometry/processing/ref.bib',
	'rendering/shading/ref.bib',
  'getting-started/drawing-2d/ref.bib',
  'getting-started/curves/ref.bib',
  'getting-started/images/ref.bib',
	'rendering/global-illum/ref.bib',
	'animation/elastomers/ref.bib',
	'animation/rigid-bodies/ref.bib',
	'animation/fluids/ref.bib',
	'visualization/informational/ref.bib',
	'visualization/basics/ref.bib',
	'visualization/scientific/ref.bib',
	'interaction/basics/ref.bib',
	'interaction/spatial/ref.bib',
	'visualization/analytics/ref.bib'
]

myst_enable_extensions = [
    'dollarmath',
	'amsmath'
]

myst_dmath_double_inline = True