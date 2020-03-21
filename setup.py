import re
import setuptools

PACKAGE = 'threadex'

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('{}/__init__.py'.format(PACKAGE), 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setuptools.setup(
    name=PACKAGE,
    version=version,
    author="denaltro",
    author_email="denaltro@gmail.com",
    description="Small extension for default Python threads",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/denaltro/threadex",
    packages=setuptools.find_packages(exclude=["tests.*", "tests", "local*"]),
    include_package_data=True,
    python_requires='>=3.6',
)
