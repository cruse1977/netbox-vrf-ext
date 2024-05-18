import codecs
import os.path

from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='netbox-vrf-ext',
    version=get_version('netbox_vrf_ext/version.py'),
    description='NetBox VRF extensions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cruse1977/netbox-vrf-ext',
    author='Chris Russell',
    author_email='cruse1977123@gmail.com',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    keywords=["netbox-plugin"],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    "Programming Language :: Python :: 3 :: Only",
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    ],
    project_urls={
        "Source": "https://github.com/cruse1977/netbox-vrf-ext",
    },
)
