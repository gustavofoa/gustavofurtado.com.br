#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gustavo Furtado'
SITEURL = 'http://localhost:1337'
SITENAME = 'Gustavo Furtado de Oliveira Alves'
SITETITLE = SITENAME
SITESUBTITLE = 'Desenvolvedor de Softwares'
SITEDESCRIPTION = 'Blog do Gustavo Furtado de Oliveia Alves'
SITELOGO = SITEURL + '/images/profile.jpg'
FAVICON = SITEURL + '/images/favicon/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

PATH = 'content'


# Enable i18n plugin.
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#language
TIMEZONE = 'America/Sao_Paulo'
# I18N_TEMPLATES_LANG = 'pt_BR'
# DEFAULT_LANG = 'pt_BR'
# OG_LOCALE = 'pt_BR'
# LANGUAGE = 'pt_BR'
# LOCALE = 'pt_BR'
# Default theme language.
I18N_TEMPLATES_LANG = 'pt_BR'
# Your language.
DEFAULT_LANG = 'pt_BR'
OG_LOCALE = 'pt_BR'
LOCALE = ('pt','bra', 'pt_BR')
LANGUAGE = 'pt_BR'

DEFAULT_DATE_FORMAT = '%d de %B de %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://br.linkedin.com/in/gustavo-furtado-ab5703a'),
          ('github', 'https://github.com/gustavofoa'),
          ('google', 'https://google.com/+GustavoFurtadoDeOliveiraAlves'),
          ('twitter', 'https://twitter.com/gustavofoa'),
          ('rss', '//gustavofurtado.com.br/feeds/all.atom.xml'))
DEFAULT_PAGINATION = 10

MENUITEMS = (('Arquivo', '/archives.html'),
             ('Categorias', '/categories.html'),
             ('Tags', '/tags.html'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'theme'


BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

STATIC_PATHS = ['images', 'extra/CNAME', 'static']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'},
}

CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

DISQUS_SITENAME = 'gustavofurtado'
GOOGLE_ANALYTICS = 'UA-36232166-2'
GOOGLE_TAG_MANAGER = ''

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-6041601556788047',    # Your AdSense ID
    'page_level_ads': True,          # Allow Page Level Ads (mobile)
    'ads': {
        'aside': '',          # Side bar banner (all pages)
        'main_menu': '',      # Banner before main menu (all pages)
        'index_top': '8686634979',      # Banner after main menu (index only)
        'index_bottom': '8686634979',   # Banner before footer (index only)
        'article_top': '8686634979',    # Banner after article title (article only)
        'article_bottom': '8686634979', # Banner after article content (article only)
    }
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
