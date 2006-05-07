#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='Mirage',
        version='0.6',
        description='A simple GTK+ image viewer',
        author='Scott Horowitz',
        author_email='stonecrest@gmail.com',
        url='http://www.theskyiscrape.com/scott/mirage.html',
        classifiers=[
            'Environment :: X11 Applications',
            'Intended Audience :: End Users/Desktop',
            'License :: GNU General Public License (GPL)',
            'Operating System :: Linux',
            'Programming Language :: Python',
            'Topic :: Multimedia :: Graphics :: Viewers'
            ],
        py_modules = ['mirage'],
	ext_modules = [Extension('imgfuncs', ['imgfuncs.c'])],
        scripts = ['mirage'],
        data_files=[('share/mirage', 
                        ['README', 'COPYING', 'CHANGELOG']),
                    ('share/applications',
                        ['mirage.desktop']),
                    ('share/pixmaps',
                        ['mirage.png', 'mirage_large.png'])],
        )
