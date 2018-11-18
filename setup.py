import setuptools

with open('README.md', 'r') as rm:
	long_description = rm.read()

setuptools.setup(
	name='databricksapi',
	version='1.0.5',
	description='Python Databricks API wrapper using requests module',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Angel Hernandez',
	url='https://github.com/angel-hernandez91/databricks_api',
	author_email='ahernandez0691@gmail.com',
	license='MIT',
	packages=setuptools.find_packages(),
	zip_safe=False,
	classifiers= [
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	]


	)