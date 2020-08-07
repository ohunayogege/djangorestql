import pathlib
from setuptools import setup

# The directory containing this file
PATH = pathlib.Path(__file__).parent

# The text of the README file
README = (PATH/"README.md").read_text()

# This call to setup() does all the work
setup(
   name="djangorestql",
   version="1.0.1",
   platform="Django",
   summary="You can now use GraphQL with Django RestFramework (DRF) on your API like PRO",
   long_description=README,
   long_description_content_type="text/markdown",
   home_page="https://djangorestql.ohunayogege.com",
   author="Ohunayo Gege",
   author_email="ohunayogege@gmail.com",
   license="MIT",
   classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
   ],
   packages=["djangorestql"],
   includepackagedata=True,
   installrequires=["django","djangorestframework","pypeg2"],
   include_package_data=True,
 )
