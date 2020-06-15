import io
from setuptools import find_packages, setup


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='eayenv',
      version='0.1',
      description='',
      long_description=long_description(),
      long_description_content_type="text/markdown",
      url='https://github.com/brunocampos01/easyenv',
      author='Bruno Campos',
      author_email="brunocampos01@gmail.com",
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          ],
      zip_safe=False)
