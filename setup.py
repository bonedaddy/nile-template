from setuptools import setup

setup(
   name='nile-template',
   version='1.0',
   description='Cairo project template using nile',
   author='Bonedaddy',
   author_email='catch@bonedaddy.io',
   packages=['app', 'tests'],  #same as name
   install_requires=['cairo-nile', 'openzeppelin-cairo-contracts', 'marshmallow-dataclass==8.5.3'], #external packages as dependencies
)
