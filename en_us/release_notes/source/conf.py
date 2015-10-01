# -*- coding: utf-8 -*-
#

import sys, os

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

master_doc = 'index'

# The suffix of source filenames.
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'



# Add any paths that contain templates here, relative to this directory.
#templates_path.append('source/_templates')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path.append('source/_static')

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = 'edx_theme'

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
html_theme_path = ['../../_themes']

html_favicon = '../../_themes/edx_theme/static/css/favicon.ico'

#html_use_smartypants = True
html_use_smartypants = True

if on_rtd:
    html_context = {
       "on_rtd" : on_rtd,
       "google_analytics_id" : '',
       "disqus_shortname" : 'edx',
       "github_base_account" : 'edx',
       "github_project" : 'edx-documentation',
    }

# General information about the project.
project = u'edX Release Notes'
copyright = u'2015, edX'

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

#remove directory when content is first added to it, and add to index
exclude_patterns = ['links.rst', 'reusables/*', '2015/analytics/*2015.rst', 
                    '2015/discussions/*2015.rst', '2015/documentation/*2015.rst',
                    '2015/insights/*2015.rst', '2015/lms/*2015.rst',
                    '2015/mobile/*2015.rst', '2015/openedx/*2015.rst', 
                    '2015/ora/*2015.rst', '2015/studio/*2015.rst',
                    '2015/website/*2015.rst', '2015/xblocks/*2015.rst']