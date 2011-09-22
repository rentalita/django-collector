# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='collector', version='2.0.1',
      packages=find_packages('src/python'), package_dir={'': 'src/python'},
      author='Software 6',
      author_email='hello@software6.net',
      description='Collect email addresses to tell people when a start-up has launched.',
      url='https://github.com/software6/django-collector',
)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
