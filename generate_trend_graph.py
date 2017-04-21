# -*- coding: utf-8 -*-
"""
    :py:mod:`generate_trend_graph`
    ==============================
    
    A module to generate a SVG file from events data file.

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
import ast
import click
import svgwrite as svgwrite


def read_data_from_file(input_file, start_time, end_time):
    # todo: remove filtered_data_dict
    filtered_data_dict = []
    filtered_data_list = []
    last_read_timestamp = None
    last_status = False
    width = 0
    try:
        for line in input_file:
            #todo: make a function to return time_stamp and status!
            split_data = line.split()
            time_stamp = int(split_data[0])
            if time_stamp > end_time:
                break
            status = ast.literal_eval(split_data[1])
            if time_stamp >= start_time:
                filtered_data_dict.append([time_stamp, status])

                if last_read_timestamp:
                    width += time_stamp - last_read_timestamp
                    if last_status != status:
                        #todo: remove print
                        print width, last_status
                        filtered_data_list.append([width, last_status])
                        width = 0

                last_read_timestamp = time_stamp
                last_status = status

        if last_read_timestamp:
            width += end_time - last_read_timestamp
            if width > 0:
                filtered_data_list.append([width, last_status])

    except Exception, e:
        print('Incorrect datafile format! {0}'.format(e))
        exit()

    # todo: remove print
    print filtered_data_dict
    return filtered_data_list


def make_svg_from_data(list_of_data):
    dwg = svgwrite.Drawing('test.svg')
    dwg.viewbox(0, 0, 500, 50)
    # todo: how to show if there r a lot of data ? and their width be very tiny ? maybe svg can handle automaticly?
    # todo: width should be a percentage of 500 and also based on total
    last_width = 0
    for width, status in list_of_data:
        fill_color = 'red'
        if status:
            fill_color = 'green'

        dwg.add(dwg.rect((last_width, 0), (width, 50), fill=fill_color))
        last_width += width

    dwg.save()


@click.command()
@click.argument('start_time', type=click.IntRange(min=0))
@click.argument('end_time', type=click.IntRange(min=0))
@click.argument('input_data_file', type=click.File())
@click.argument('output_svg_file', type=click.Path())
def main(start_time, end_time, input_data_file, output_svg_file):
    list_of_filtered_events_width = read_data_from_file(input_data_file, start_time, end_time)
    print list_of_filtered_events_width
    make_svg_from_data(list_of_filtered_events_width)

if __name__ == '__main__':
    main()
