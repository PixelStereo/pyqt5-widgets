#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is an example of a device
with I/O communication provided by libossia
"""

from pyossia import *

# create the OSSIA Device with the name provided
# here for test purpose
my_device = ossia.LocalDevice('PyOssia Test Device')
my_device.expose(protocol='oscquery', listening_port=4567, sending_port=6789, logger=True)
#my_device.expose(protocol='osc', listening_port=11111, sending_port=22222, logger=False)
my_int = my_device.add_param('test/numeric/int', value_type='int', default_value=66, domain=[-100, 100])
#my_float = my_device.add_param('test/numeric/float', value_type='float', default_value=0.123456789, domain=[-2, 2.2])
#my_vec2f = my_device.add_param('test/list/vec2f', value_type='vec2f', default_value=[0.5, 0.5])
#my_vec3f = my_device.add_param('test/list/vec3f', value_type='vec3f', default_value=[-960, -270, 180],  domain=[0, 360])
#my_vec4f = my_device.add_param('test/list/vec4f', value_type='vec4f', default_value=[0, 0.57, 0.81, 0.7],  domain=[0, 1])
#my_bool = my_device.add_param('test/special/bool', value_type='bool', default_value=True, repetitions_filter=True)
#my_string = my_device.add_param('test/string', value_type='string', default_value='Hello world !', domain=['once', 'loop'])
#my_list = my_device.add_param('test/list', value_type='list', default_value=[44100, "my_track.wav", 0.6])
#my_char = my_device.add_param('test/special/char', value_type='char', default_value=chr(97))

my_device.root_node.init()




if __name__ == "__main__":
    from time import sleep
    while True:
        sleep(0.1)
