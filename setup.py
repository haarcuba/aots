from setuptools import setup, find_packages

README = 'AOTS - Art of the State - a state machine library'

requires = []
tests_require = [
        'pytest',
        ]

setup(name='aots',
      version='0.0.1',
      description=README,
      long_description=README,
      url='https://github.com/haarcuba/aots.git',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Yoav Kleinberger',
      author_email='haarcuba@gmail.com',
      keywords=[ 'statemachine', 'state machine' ],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points={
      },
      )
