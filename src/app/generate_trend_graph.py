# -*- coding: utf-8 -*-
"""
    :py:mod:`generate_trend_graph`
    ==============================

    A module to generate a SVG file from events data file.

    ----

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
import click

from utilities import get_filtered_elements_width_and_color_from_events, make_svg_from_data


@click.command()
@click.argument('start_time', type=click.IntRange(min=0))
@click.argument('end_time', type=click.IntRange(min=0))
@click.argument('input_data_file', type=click.File('r'))
@click.argument('output_svg_file', type=click.Path())
def app(start_time, end_time, input_data_file, output_svg_file):
    if end_time < start_time:
        click.echo('Error: END_TIME can\'t be less than START_TIME!')
        exit(1)
    try:
        list_of_graph_elements = get_filtered_elements_width_and_color_from_events(input_data_file,
                                                                                   start_time,
                                                                                   end_time)
        total_width = end_time - start_time
        make_svg_from_data(list_of_graph_elements, total_width, output_svg_file)
    except Exception, e:
        click.echo('Error: {0}'.format(e))
        exit(1)


if __name__ == '__main__':
    app()
