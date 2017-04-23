# -*- coding: utf-8 -*-
"""
    :py:mod:`~src.tests.generate_trend_graph_tests`
    ====================================

    Tests module for :py:mod:`~app.generate_trend_graph`.

    ----

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
from os import path

from click.testing import CliRunner
from testfixtures import TempDirectory

from ..app.generate_trend_graph import app
from . import AppTestCase


class GenerateTrendGraphTestCase(AppTestCase):
    """Test suite for :py:mod:`~app.generate_trend_graph` click application."""
    def test_application_works_correctly(self):
        """Test click application works correctly"""
        runner = CliRunner()
        with TempDirectory() as test_dir:
            test_dir.write('test.txt', '1 True')
            result = runner.invoke(app, ['1', '5',
                                         '{0}/test.txt'.format(test_dir.path),
                                         '{0}/output_test.svg'.format(test_dir.path)])
            self.assertEqual(result.exit_code, 0, msg=result.exception)
            self.assertTrue(path.exists('{0}/output_test.svg'.format(test_dir.path)))

    def test_non_zero_exit_code_for_invalid_input_file(self):
        """Test click application returns non zero exit code if invalid input file"""
        runner = CliRunner()
        with TempDirectory() as test_dir:
            test_dir.write('test.txt', 'INVALID VALUE')
            result = runner.invoke(app, ['1', '5',
                                         '{0}/test.txt'.format(test_dir.path),
                                         '{0}/output_test.svg'.format(test_dir.path)])
            self.assertEqual(result.exit_code, 1, msg=result.exception)

    def test_non_zero_exit_code_for_end_time_less_than_start_time(self):
        """Test click application returns non zero exit code if 
        end_time is less than start_time """
        runner = CliRunner()
        with TempDirectory() as test_dir:
            test_dir.write('test.txt', '1 True')
            result = runner.invoke(app, ['5', '1',
                                         '{0}/test.txt'.format(test_dir.path),
                                         '{0}/output_test.svg'.format(test_dir.path)])
            self.assertEqual(result.exit_code, 1, msg=result.exception)
