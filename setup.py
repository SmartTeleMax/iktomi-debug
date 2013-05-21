# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="iktomi.debug",
    version="",
    packages=["iktomi.debug"],
    package_data={
        '':["*.html"]
    },
    requires=[
        'webob (>1.1b1)',
        'iktomi (>0.3)',
    ],
    author="Harut Dagesyan",
    author_email="yes@harutune.name",
    description="Simple Django-style debugger for iktomi.",
    url='http://github.com/SmartTeleMax/iktomi-debug/',
    license="MIT",
    keywords="debug web",
)
