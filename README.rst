.. -*- coding: utf-8 -*-


.. _README:

**generate_trend_graph** README
===============================

This application generates trend graph from input data and store it in a SVG file.



Compatibility
-------------

**Python Runtime**
    ``python>=2.7``
    ``pip==9.0.1``
    ``virtualenv==15.1.0``



Usage
-----

Installing
^^^^^^^^^^

* Unpack the package in a directory.
* Make sure virtualenv and pip are installed before.
* Create a virtual environment:
    $: virtualenv venv

* Active the virtual environment:
    $: source venv/bin/activate

* Install requirments:
    (venv) $: pip install -r requirments.txt

It's ready to run.

Running
^^^^^^^

Below command shows the syntax usage:

    (venv) $: python src/generate_trend_graph.py --help



Running Tests
-------------

Below command runs the unit tests:

    (venv) $: nosetest -v src/tests


