from setuptools import setup, find_packages

setup(
	name='excelutils',
	author='William H. Hilska',
	author_email='whilska@gmail.com',
	version='0.9.1',
	packages=find_packages(),
	install_requires=['hilskapy', 'openpyxl']
)
