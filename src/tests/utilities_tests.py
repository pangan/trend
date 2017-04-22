# -*- coding: utf-8 -*-
"""
    :py:mod:`~src.tests.utilities_tests`
    ====================================

    Tests module for :py:mod:`~app.utilities`.

    ----

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
from random import randrange

from ..app.utilities import (_bool_to_string_color,
                             _get_timestamp_and_status_color_from_event_string,
                             get_filtered_elements_width_and_color_from_events)

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

    def test_get_timestamp_and_status_color_from_event_string_raises_exception(self):
        """Test _get_timestamp_and_status_color_from_event_string
         raises exception for invalid data"""
        for invalid_data in [None, 123, 'INVALID', '123 DATA', 'TIME True', '123 true']:
            with self.assertRaisesRegexp(Exception,
                                         'Invalid event record: {0}'.format(invalid_data)):
                _get_timestamp_and_status_color_from_event_string(invalid_data)

    def test_get_filtered_status_width_and_color_from_file_return_correct_values(self):
        """Test get_filtered_status_width_and_color_from_file returns correct values"""
        test_events_list = [
            '2 True',
            '5 False',
            '7 True'
        ]
        expected_elements = [
            [1, 'white'],
            [3, 'green'],
            [2, 'red'],
            [4, 'green']
        ]
        test_elements = get_filtered_elements_width_and_color_from_events(test_events_list, 1, 11)
        self.assertItemsEqual(expected_elements,test_elements)

    def test_make_svg_from_data(self):
        """todo:write comment"""
        pass
