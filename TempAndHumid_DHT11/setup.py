try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project'
    , 'author': 'Jason Baumbach'
    , 'url': 'http://???'
    , 'download_url': 'http://???'
    , 'author_email': 'jatlast@hotmail.com'
    , 'version': '0.1'
    , 'install_requires': ['nose']
    , 'packages': ['NAME']
    , 'scripts': []
    , 'name': 'projectname'
}

setup(**config)

