"""
Check IPs

Description:
* Search .csv for all values that match regex [\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}
* Ping IPs
* Return passing IPs
* Return failing IPs

Author: Nic La
Last modified: Sep 2021
"""

import os
import csv
import re


def read_in_ips(input_file):
    """Read in IPs from CSV"""
    raw = []
    ips = []
    pattern = r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}'

    with open(input_file) as in_file:
        reader = csv.reader(in_file, delimiter=',')
        for row in reader:
            raw.append(row)

    for line in raw:
        for item in line:
            match = re.search(pattern, item)
            if match is not None:
                ips.append(match[0])
    return ips


def ping_ip(ip):
    """Ping IP and wait"""
    proc = os.popen(f'ping {ip}').read()
    return proc


def print_report(ip, raw_out):
    """Report passing/failing IPs"""
    pattern = r'Reply from '
    match = re.search(pattern, raw_out)
    if match is not None:
        print(f'{ip} PASS')
    else:
        print(f'{ip} FAIL')


if __name__ == '__main__':
    input_file = 'input_file.csv'
    ips = read_in_ips(input_file)
    for ip in ips:
        out = ping_ip(ip)
        print_report(ip, out)
