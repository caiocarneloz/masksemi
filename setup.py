from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='masksemi',
    version='0.0.1',
    url='https://github.com/caiocarneloz/masksemi',
    license='MIT License',
    author='Caio Carneloz',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=['semi-supervised', 'label', 'preprocessing'],
    description=u'Code for converting a list of labels in a scikit-like semi-supervised labels.',
    packages=['masksemi'],
    install_requires=[],)