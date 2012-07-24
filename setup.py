# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="insdebug",
    version="",
    packages=["insdebug"],
    package_data={
        '':["*.html"]
    },
    requires=[
        "insanities",#
        'webob',
        "jinja2",# template engine
    ],
    author="Harut Dagesyan",
    author_email="yes@harutune.name",
    description="Simple Django-style web output of debug information for insanities.",
    license="MIT",
    keywords="debug web",
)
