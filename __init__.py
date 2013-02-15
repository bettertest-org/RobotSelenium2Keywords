# -*- coding: utf-8 -*-
from keywords import *


class Selenium2LibraryExtensions(
        _CssKeywords

):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '0.0.1'

    def __init__(self, timeout=5.0, implicit_wait=0.0, run_on_failure='Capture Page Screenshot'):
        for base in Selenium2LibraryExtensions.__bases__:
            if hasattr(base,'__init__'):
                base.__init__(self)

