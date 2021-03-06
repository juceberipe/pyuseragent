from setuptools import setup

setup(name='useragent',
      version='0.1',
      description='A useragent parser for Python.',
      url='http://github.com/snormore/pyuseragent',
      author='Steven Normore',
      author_email='snormore@gmail.com',
      license='Apache',
      packages=['useragent'],
      package_data={'useragent': ['data/*', ]},
      include_package_data=True)