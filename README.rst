============
INSDEBUG
============

Simple debugger for insanities, based on Django debug.

Usage
=====

Create ``manage_local.py`` with following contents::

    #!./venv/bin/python
    from manage import run
    from app import app as old_app
    from insane_debug import debug
    from insanities import web

    app = web.handler(debug) | old_app

    if __name__ == '__main__':
        run(app)

