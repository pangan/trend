# -*- coding: utf-8 -*-
"""
    :py:mod:`generate_trend_graph`
    ==============================
    
    A module to generate a SVG file from events data file.

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
import ast
import click
import svgwrite


def _bool_to_color(bool_value):
    if bool_value:
        return 'green'
    return 'red'


def _get_timestamp_and_status_color_from_data_string(data_string):
    split_data = data_string.split()
    time_stamp = int(split_data[0])
    status_color = _bool_to_color(ast.literal_eval(split_data[1]))
    return time_stamp, status_color


def read_data_from_file(input_file, start_time, end_time):
    filtered_data_list = []
    last_read_timestamp = start_time
    last_status = 'white'
    # todo: write comment why white is used!
    width = 0
    try:
        for line in input_file:
            time_stamp, status_color = _get_timestamp_and_status_color_from_data_string(line)
            if time_stamp > end_time:
                break

            if time_stamp >= start_time:
                width += time_stamp - last_read_timestamp
                if last_status != status_color:
                        filtered_data_list.append([width, last_status])
                        width = 0

                last_read_timestamp = time_stamp
                last_status = status_color

        width += end_time - last_read_timestamp
        if width > 0:
            filtered_data_list.append([width, last_status])

    except Exception, e:
        print('Incorrect datafile format! {0}'.format(e))
        exit()

    return filtered_data_list


def make_svg_from_data(list_of_data, total_width):
    # todo: make output file from parameter!
    dwg = svgwrite.Drawing('test.svg')
    maximum_viewbox_width = 500.0
    dwg.viewbox(0, 0, maximum_viewbox_width, 50)
    last_width = 0
    for width, status_color in list_of_data:
        percentage_width = width * maximum_viewbox_width / total_width
        dwg.add(dwg.rect((last_width, 0), (percentage_width, 50), fill=status_color))
        last_width += percentage_width

    dwg.save()


@click.command()
@click.argument('start_time', type=click.IntRange(min=0))
@click.argument('end_time', type=click.IntRange(min=0))
@click.argument('input_data_file', type=click.File())
@click.argument('output_svg_file', type=click.Path())
def main(start_time, end_time, input_data_file, output_svg_file):
    list_of_filtered_events_width = read_data_from_file(input_data_file, start_time, end_time)
    print list_of_filtered_events_width
    total_width = end_time - start_time
    make_svg_from_data(list_of_filtered_events_width, total_width)

if __name__ == '__main__':
    main()
