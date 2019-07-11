#!/usr/local/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Dmytro Pavlyuk'

import requests
import time
from sys import exit, argv

if len(argv) == 1:
    print('Не заданий аргумент: on/off')
    exit()
else:
    arg = argv[1]

url = 'http://192.168.1.1/apply.cgi'
if arg == 'on' or arg == 'off':
    if arg == 'on':
        data = {'submit_button': 'Wireless_MAC',
                'change_action': '',
                'action': 'Apply',
                'wl_macmode': 'disabled',
                'wl_maclist': 50,
                'wait_time': 3,
                'nvset_cgi': 'wireless',
                'wl_mac_filter': 0}

    elif arg == 'off':
        data = {'submit_button': 'Wireless_MAC',
                'change_action': '',
                'action': 'Apply',
                'wl_macmode': 'deny',
                'wl_maclist': 50,
                'wait_time': 3,
                'nvset_cgi': 'wireless',
                'wl_mac_filter': 1,
                'start': '',
                'wl_macmode1': 'deny',
                # 'm0': '00:09:4C:F7:55:1C', # планшет зелений
                # 'm1': 'B8:B4:2E:46:AF:70', # телефон Яріка
                # 'm2': '4C:ED:DE:CC:32:F2', # компьютер Оленки
                # 'm3': 'B8:B4:2E:3C:3F:D2', # телефон Олі Fly
                'm1': 'D8:6C:02:9E:8D:6C', # телефон Оленки м5с
                'm2': '40:C6:2A:2E:53:46', # телефон Яріка MEIZU M2
                # 'm3': '00:16:CF:40:01:56', # телефон Олі MEIZU M6
                'm4': 'B0:FC:36:29:48:35', # компьютер Оленки
                # 'm5': '0C:D2:92:AC:B5:84', # мій комп Lenovo
                # 'm6': 'FC:53:9E:AB:AA:03' # m5s
                'end': ''}

    try:
        response = requests.post(url, data,  auth=('admin', 'admin'), stream=True)
        print('\n=============== SUCSESS =================\n')

        # content = response.content.decode('utf-8')

    except requests.exceptions.HTTPError:
        print("Ooops! HTTP Error!")
        exit()

    except requests.exceptions.ConnectionError as err:
        print("Ooops! Connection Error. Check the connection")
        print('Response is: ', err)
        print('Done')
        exit()

time.sleep(5)