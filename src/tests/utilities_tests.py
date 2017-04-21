# -*- coding: utf-8 -*-
"""
    :py:mod:`~src.tests.utilities_tests`
    ====================================

    Tests module for :py:mod:`~app.utilities`.

    ----

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
from random import randrange

from ..app.utilities import (_bool_to_string_color, _get_timestamp_and_status_color_from_event_string)

from . import AppTestCase


class UtilitiesTestCase(AppTestCase):
    """Test suite for :py:mod:`~app.utilities` module functions."""
    def test_bool_to_string_color(self):
        """Test _bool_to_string_color returns correct value"""
        self.assertEquals(_bool_to_string_color(True), 'green')
        self.assertEquals(_bool_to_string_color(False), 'red')

    def test_get_timestamp_and_status_color_from_event_string(self):
        """Test _get_timestamp_and_status_color_from_event_string"""
        expected_timestamp = randrange(1000)
        test_timestamp, test_status_color = _get_timestamp_and_status_color_from_event_string(
            '{0} True'.format(expected_timestamp))
        self.assertEquals(test_timestamp, expected_timestamp)
        self.assertEquals(test_status_color, 'green')

    def test_read_data_from_file(self):
        """todo:write comment"""
        pass

    def test_read_data_from_file_raise_exception_on_invalid_file(self):
        """todo:write comment"""
        pass

    def test_make_svg_from_data(self):
        """todo:write comment"""
        pass
