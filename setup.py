from setuptools import setup, find_packages

setup(
    name='express-template-257',
    version='0.9.80',
    packages=find_packages(),
    install_requires=['requests>=2.28.0', 'click>=8.0'],
    entry_points={'console_scripts': ['express-template-257=expresstemplate:main']},
)
