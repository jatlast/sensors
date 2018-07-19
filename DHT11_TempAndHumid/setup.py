try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'DHT11 (DHT Eleven) Temperature & Humidity Sensor'
    , 'author': 'Jason Baumbach'
    , 'url': 'http://https://github.com/jatlast/sensors/tree/master/TempAndHumid_DHT11/DHTEleven'
    , 'download_url': 'https://github.com/jatlast/sensors/tree/master/TempAndHumid_DHT11/DHTEleven'
    , 'author_email': 'jatlast@hotmail.com'
    , 'version': '0.1'
    , 'install_requires': ['nose']
    , 'packages': ['DHT11']
    , 'scripts': []
    , 'name': 'sensors/DHTEleven'
}

setup(**config)

