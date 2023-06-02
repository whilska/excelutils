from setuptools import setup, find_packages

setup(
	name='fantasyfootball',
	author='William H. Hilska',
	author_email='whilska@gmail.com',
	version='0.9.0',
	packages=find_packages(),
	install_requires=['hilskapy', 'openpyxl']
)
