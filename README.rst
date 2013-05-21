============
iktomi.debug
============

Simple debugger for iktomi, based on Django debug.

Usage
=====

Prepend debug handler to your app::

    from iktomi.debug import debug

    app = debug | old_app

Caution! Do not use on production!
