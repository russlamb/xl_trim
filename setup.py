from setuptools import setup

setup(name="xl_trim",
		version='0.2.6',
		description='Trim top rows from an Excel file',
		url='',
		author='Russ Lamb',
		author_email='lamb.russell@gmail.com',
		license='MIT',
		py_modules=['xl_trim'],
		zip_safe=False,
		install_requires=['pandas','pytz','six','python-dateutil','numpy','xlrd','xlwt'])