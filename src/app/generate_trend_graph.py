# -*- coding: utf-8 -*-
"""
    :py:mod:`generate_trend_graph`
    ==============================
    
    A module to generate a SVG file from events data file.

    ----
    
    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
import click

from utilities import read_data_from_file, make_svg_from_data


@click.command()
@click.argument('start_time', type=click.IntRange(min=0))
@click.argument('end_time', type=click.IntRange(min=0))
@click.argument('input_data_file', type=click.File())
@click.argument('output_svg_file', type=click.Path())
def app(start_time, end_time, input_data_file, output_svg_file):
    list_of_filtered_events_width = read_data_from_file(input_data_file, start_time, end_time)
    total_width = end_time - start_time
    make_svg_from_data(list_of_filtered_events_width, total_width)

if __name__ == '__main__':
    app()
