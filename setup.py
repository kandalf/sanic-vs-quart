from setuptools import setup

setup(
  name='platappform',
  packages=['api'],
  include_package_data=True,
  install_requires=[
    'sanic',
    'gino'
  ],
)
