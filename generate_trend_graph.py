# -*- coding: utf-8 -*-
"""
    :py:mod:`generate_trend_graph`
    ==============================
    
    A module to generate a SVG file from events data file.

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
import click


def read_data_from_file(input_file):
    return []

@click.command()
@click.argument('start_time', type=click.IntRange(min=0))
@click.argument('end_time', type=click.IntRange(min=0))
@click.argument('input_data_file', type=click.File())
@click.argument('output_svg_file', type=click.Path())
def main(start_time, end_time, input_data_file, output_svg_file):
    list_of_events = read_data_from_file(input_data_file)
    print list_of_events


if __name__ == '__main__':
    main()
