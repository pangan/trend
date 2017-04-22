# -*- coding: utf-8 -*-
"""
    :py:mod:`src.tests`
    ===================

    Test package for the :py:mod:`app`.

    ----

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""

from unittest import TestCase


class AppTestCase(TestCase):
    """Abstract base class for all :py:mod:`app` test cases."""
    def setUp(self):
        super(AppTestCase, self).setUp()

    def tearDown(self):
        super(AppTestCase, self).tearDown()
