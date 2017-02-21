# vim:ts=4:sw=4:
import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name='tkwidgettree',
	version='1.0.0b1',
	author='Staffan Thomen',
	author_email = 'duck@shangtai.net',
	description = ('Convenience class for building Tk widgets trees from a dict or a JSON file'),
	license = 'BSD',
	keywords = 'Tk tkinter widget builder',
	packages=[ 'tkwidgettree' ],
	long_description=read('README'),
	classifiers = [
		'Development status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Programming Language :: Python 2.7',
		'Programming Language :: Python 3'
	]
);
