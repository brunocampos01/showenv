import os
from setuptools import find_packages
from setuptools import setup


try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements


HERE = os.path.abspath(os.path.dirname(__file__))
requirements_path = os.path.join(HERE, 'requirements.txt')
install_reqs = parse_requirements(requirements_path, session=False)

try:
    requirements = [str(ir.req) for ir in install_reqs]
except AttributeError:
    requirements = [str(ir.requirement) for ir in install_reqs]

# The text of the README file
with open(os.path.join(HERE, "README.md")) as f:
    README = f.read()

setup(name='showenv',
      version='1.0',
      packages=find_packages(),
      include_package_data=True, # add *sh
      scripts=['showenv/scripts/show_config_environment.sh',
               'showenv/scripts/show_structure_project.sh',
               'showenv/scripts/config_environment.txt',
               'showenv/scripts/struture_project.txt',
               'showenv/scripts/test_env.py'],
      install_requires=requirements,
      entry_points={
          "console_scripts": ["showenv=showenv.__main__:main"]
      },
      description='Show informations about project, python, pip, libraries and OS',
      long_description=README,
      long_description_content_type="text/markdown",
      url='https://github.com/brunocampos01/showenv',
      author='Bruno Campos',
      author_email="brunocampos01@gmail.com",
      license='MIT',
      platforms='linux',
      classifiers=[
          'Programming Language :: Python',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License'
          ],
      zip_safe=False)
