#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from insanities.web.core import RequestHandler
from webob.exc import HTTPException
from insanities.http import Response
from debug_dj import technical_500_response

import logging
logger = logging.getLogger(__name__)

def debug(env, data, next_handler):
    try:
        return next_handler(env, data)
    except HTTPException, e:
        return e
    except Exception, e:
        exc_info = sys.exc_info()
        html = technical_500_response(env, *exc_info)
        logger.exception(e)
        return Response(html, 500)

