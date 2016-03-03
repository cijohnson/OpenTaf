from setuptools import setup, find_packages

import opentaf

version = opentaf.__version__
readme = open('README.md').read()


def requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


setup(name="opentaf",
      version=version,
      packages=find_packages(),
      author='Ignatious Johnson Christopher',
      author_email='ignajohn@gmail.com',
      description='Open Test Automation Framework',
      keywords='automation framework infrastructure executer',
      long_description=readme,
      install_requires=requirements('requirements.txt'),
      entry_points={
          'console_scripts': [
              'opentaf = opentaf.main:main',
          ],
      },
      license='Free',
      url='',
      )
