# -*- coding: utf-8 -*-
"""
    :py:mod:`~app.utilities`
    ==============================

    A collection of utilities used by main application.

    ----

    .. moduleauthor:: Amir Mofakhar <pangan@gmail.com>

"""
import ast
import svgwrite


def _bool_to_string_color(bool_value):
    if bool_value:
        return 'green'
    return 'red'


def _get_timestamp_and_status_color_from_event_string(data_string):
    try:
        split_data = data_string.split()
        time_stamp = int(split_data[0])
        status_color = _bool_to_string_color(ast.literal_eval(split_data[1]))
    except Exception:
        raise (Exception('Invalid event record: {0}'.format(data_string)))

    return time_stamp, status_color


def get_filtered_elements_width_and_color_from_events(events_list, start_time, end_time):
    filtered_data_list = []
    last_read_timestamp = start_time
    last_status = 'white'
    width = 0

    for event in events_list:
        time_stamp, status_color = _get_timestamp_and_status_color_from_event_string(event)
        if time_stamp > end_time:
            break

        if time_stamp >= start_time:
            width += time_stamp - last_read_timestamp
            if last_status != status_color and width > 0:
                filtered_data_list.append([width, last_status])
                width = 0

            last_read_timestamp = time_stamp

        last_status = status_color

    width += end_time - last_read_timestamp
    if width > 0:
        filtered_data_list.append([width, last_status])

    return filtered_data_list


def make_svg_from_data(list_of_data, total_width, output_file):
    output_svg = svgwrite.Drawing(output_file)
    maximum_viewbox_width = 500.0
    output_svg.viewbox(0, 0, maximum_viewbox_width, 50)
    last_width = 0
    for width, status_color in list_of_data:
        graph_element_width = width * maximum_viewbox_width / total_width
        output_svg.add(output_svg.rect((last_width, 0),
                                       (graph_element_width, 50),
                                       fill=status_color))
        last_width += graph_element_width

    output_svg.save(pretty=True)
