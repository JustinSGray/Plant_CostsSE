#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Katherine Dykes, Andrew Ning, and George Scott',
 'author_email': 'systems.engineering@nrel.gov',
 'description' : 'NREL WISDEM plant cost models',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license' : 'Apache License, Version 2.0',
 'version' : '0.1.0',
 'name': 'Plant_CostsSE',
 'package_data': {'Plant_CostsSE': []},
 'package_dir': {'': 'src'},
 'packages': ['plant_costsse.nrel_csm_bos', 'test', 'plant_costsse.nrel_csm_opex', 'plant_costsse.ecn_offshore_opex', 'plant_costsse.nrel_land_bosse'],
 'zip_safe': False}


setup(**kwargs)

# set up for land-based bos model
from distutils.core import setup
from distutils.extension import Extension

try:
    USE_CYTHON = True
    from Cython.Build import cythonize
except Exception:
    USE_CYTHON = False


ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension('_landbos', ['src/plant_costsse/nrel_land_bosse/_landbos'+ext, 'src/plant_costsse/nrel_land_bosse/LandBOSsmooth.c'])]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name='NREL_Land_BOSSE',
    description='a translation of the NREL land-based balance of station excel model',
    author='S. Andrew Ning',
    author_email='andrew.ning@nrel.gov',
    package_dir={'': 'src'},
    py_modules=['plant_costsse.nrel_land_bosse.nrel_land_bosse'],
    license='Apache License, Version 2.0',
    ext_modules=extensions
)