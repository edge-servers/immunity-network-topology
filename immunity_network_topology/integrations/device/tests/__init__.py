SIMPLE_MESH_DATA = {
    '64:70:02:c3:03:b2': [
        {
            'mac': '64:70:02:c3:03:b3',
            'mtu': 1500,
            'multicast': True,
            'name': 'mesh0',
            'txqueuelen': 1000,
            'type': 'wireless',
            'up': True,
            'wireless': {
                'channel': 11,
                'clients': [
                    {
                        'auth': True,
                        'authorized': True,
                        'ht': True,
                        'mac': 'a4:bc:3f:ae:c7:0c',
                        'mfp': False,
                        'noise': -90,
                        'vendor': 'TP-LINK TECHNOLOGIES CO.,LTD.',
                        'vht': False,
                        'wmm': True,
                        'mesh_llid': 19000,
                        'mesh_plid': 24000,
                        'mesh_non_peer_ps': 'ACTIVE',
                    },
                    {
                        'auth': True,
                        'authorized': True,
                        'ht': True,
                        'mac': '2a:9a:fb:12:11:77',
                        'mfp': False,
                        'noise': -94,
                        'signal': -58,
                        'vendor': 'TP-LINK TECHNOLOGIES CO.,LTD.',
                        'vht': False,
                        'wmm': True,
                        'mesh_llid': 19500,
                        'mesh_plid': 24500,
                        'mesh_non_peer_ps': 'ACTIVE',
                    },
                ],
                'country': 'ES',
                'frequency': 2462,
                'htmode': 'HT20',
                'mode': '802.11s',
                'noise': -95,
                'signal': -61,
                'ssid': 'Test Mesh',
                'tx_power': 17,
            },
        }
    ],
    'a4:bc:3f:ae:c7:0b': [
        {
            'mac': 'a4:bc:3f:ae:c7:0c',
            'mtu': 1500,
            'multicast': True,
            'name': 'mesh0',
            'txqueuelen': 1000,
            'type': 'wireless',
            'up': True,
            'wireless': {
                'channel': 11,
                'clients': [
                    {
                        'auth': True,
                        'authorized': True,
                        'ht': True,
                        'mac': '64:70:02:C3:03:B3',
                        'mfp': False,
                        'noise': -98,
                        'signal': -58,
                        'vendor': 'TP-LINK TECHNOLOGIES CO.,LTD.',
                        'vht': False,
                        'wmm': True,
                        'mesh_llid': 20000,
                        'mesh_plid': 25000,
                        'mesh_non_peer_ps': 'ACTIVE',
                    },
                    {
                        'auth': True,
                        'authorized': True,
                        'ht': True,
                        'mac': '2a:9a:fb:12:11:77',
                        'mfp': False,
                        'noise': -96,
                        'signal': -60,
                        'vendor': 'TP-LINK TECHNOLOGIES CO.,LTD.',
                        'vht': False,
                        'wmm': True,
                        'mesh_llid': 19500,
                        'mesh_plid': 24500,
                        'mesh_non_peer_ps': 'ACTIVE',
                    },
                ],
                'country': 'ES',
                'frequency': 2462,
                'htmode': 'HT20',
                'mode': '802.11s',
                'noise': -95,
                'signal': -56,
                'ssid': 'Test Mesh',
                'tx_power': 17,
            },
        }
    ],
    '2a:9a:fb:12:11:76': [
        {
            'mac': '2a:9a:fb:12:11:77',
            'mtu': 1500,
            'multicast': True,
            'name': 'mesh0',
            'txqueuelen': 1000,
            'type': 'wireless',
            'up': True,
            'wireless': {
                'channel': 11,
                'clients': [
                    {
                        # Link properties
                        'auth': True,
                        'authorized': True,
                        'noise': -92,
                        'signal': -56,
                        # Node properties
                        'ht': True,
                        'mfp': False,
                        'vht': False,
                        'wmm': True,
                        'mac': 'a4:bc:3f:ae:c7:0c',
                        'vendor': 'TP-LINK TECHNOLOGIES CO.,LTD.',
                        'mesh_non_peer_ps': 'LISTEN',
                    },
                    {
                        'mac': '0a:cc:ae:34:ff:3d',
                        'wps': False,
                        'wds': False,
                        'ht': True,
                        'preauth': False,
                        'assoc': True,
                        'authorized': True,
                        'vht': False,
                        'wmm': False,
                        'aid': 1,
                        'mfp': False,
                        'auth': True,
                        'vendor': 'TP-LINK TECHNOLOGIES CO.,LTD.',
                        'signature': 'test_signature',
                        'mesh_plink': 'LISTEN',
                    },
                ],
                'country': 'ES',
                'frequency': 2462,
                'htmode': 'HT20',
                'mode': '802.11s',
                'noise': -95,
                'signal': -64,
                'ssid': 'Test Mesh',
                'tx_power': 17,
            },
        },
        {
            'addresses': [
                {
                    'address': '192.168.1.1',
                    'family': 'ipv4',
                    'mask': 24,
                    'proto': 'static',
                },
            ],
            'bridge_members': ['eth0.1', 'mesh0'],
            'mac': '2a:9a:fb:12:11:76',
            'mtu': 1500,
            'multicast': True,
            'name': 'br-lan',
            'speed': '-1F',
            'stp': False,
            'txqueuelen': 1000,
            'type': 'bridge',
            'up': True,
        },
        {
            'name': 'wlan0',
            'type': 'wireless',
            'up': True,
            'mac': '2a:9a:fb:12:11:78',
            'txqueuelen': 1000,
            'multicast': True,
            'mtu': 1500,
            'wireless': {
                'frequency': 2437,
                'mode': 'access_point',
                'signal': -29,
                'tx_power': 6,
                'channel': 6,
                'ssid': 'testnet',
                'noise': -95,
                'country': 'US',
                'htmode': 'HT20',
                'clients': [
                    {
                        'mac': '00:ee:ad:34:f5:3b',
                        'wps': False,
                        'wds': False,
                        'ht': True,
                        'preauth': False,
                        'assoc': True,
                        'authorized': True,
                        'vht': False,
                        'wmm': True,
                        'aid': 1,
                        'mfp': False,
                        'auth': True,
                        'vendor': 'TP-LINK TECHNOLOGIES CO.,LTD.',
                        'signature': 'test_signature',
                    },
                ],
            },
        },
    ],
}

SINGLE_NODE_MESH_DATA = {
    '64:70:02:c3:03:b2': [
        {
            'mac': '64:70:02:c3:03:b3',
            'mtu': 1500,
            'multicast': True,
            'name': 'mesh0',
            'txqueuelen': 1000,
            'type': 'wireless',
            'up': True,
            'wireless': {
                'channel': 11,
                'clients': [],
                'country': 'ES',
                'frequency': 2462,
                'htmode': 'HT20',
                'mode': '802.11s',
                'noise': -95,
                'signal': -61,
                'ssid': 'Test Mesh',
                'tx_power': 17,
                'mesh_llid': 19751,
                'mesh_local_ps': 'ACTIVE',
                'mesh_non_peer_ps': 'ACTIVE',
                'mesh_peer_ps': 'ACTIVE',
                'mesh_plid': 24413,
                'mesh_plink': 'ESTAB',
            },
        }
    ],
}