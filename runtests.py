#!/usr/bin/env python

import os
import sys

sys.path.insert(0, 'tests')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immunity2.settings')

if __name__ == '__main__':
    import pytest
    from django.core.management import execute_from_command_line

    args = sys.argv
    args.insert(1, 'test')
    if not os.environ.get('SAMPLE_APP', False):
        args.insert(2, 'immunity_network_topology')
        args.insert(3, 'immunity_network_topology.integrations.device')
    else:
        args.insert(2, 'immunity2')
    if os.environ.get('WIFI_MESH', False):
        args.extend(['--tag', 'wifi_mesh'])
    else:
        args.extend(['--exclude-tag', 'wifi_mesh'])
execute_from_command_line(args)
sys.exit(
    pytest.main(
        [os.path.join('immunity_network_topology', 'tests', 'test_websockets.py')]
    )
)
