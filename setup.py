import os
from distutils.core import setup
import simpropy

setup(
    name='simpropy',
    version=simpropy.__version__,
    description='Python wrapper for the SimPro API - http://api.simpro.co/',
    license='MIT',
    keywords='SimPro',
    packages=['simpropy'],
    install_requires=['requests_oauthlib'],
    long_description=(open('README.rst').read() if os.path.exists('README.rst') else ''),
)
