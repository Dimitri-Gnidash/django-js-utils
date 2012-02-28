from setuptools import setup, find_packages

DESCRIPTION = 'A small JavaScript utility library for use with Django projects.'

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

setup(name='django-js-utils',
      version='0.1',
      packages=find_packages(exclude=('tests', 'tests.*',
                                      'base_project', 'base_project.*')),
      author='Marco Louro and others',
      author_email='hello@mlouro.com',
      url='https://github.com/Dimitri-Gnidash/django-js-utils',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: BSD License',
      ],
)
