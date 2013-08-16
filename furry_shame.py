#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GPLv3

# (c) 2013 Ville Korhonen <ville@xd.fi>

import os
import sys
import json
import requests
import argparse
import logging
import subprocess


WEBVM_API_URL = 'http://nm.0xff.fi/api/v1'

WEBVM_CONFIG_PATH = '~/.config/webvm'

# TODO: If config file doesn't exist, create it (using defaults + cli args)

class WebVMClient(object):
    def __init__(self, url, *args, **kwargs):
        self._api_url = url
    
    # TODO: Allow user to log-in w/ username+password & fetch OAuth token
    
    def cmd_register(self):
        # TODO: Register as a new slave, submit SSH key
        # TODO: Create SSH key
        # cmd = ['ssh-keygen', '-q', '-t', 'rsa', '-C', 'WebVM Slave key for %s' % slaveid, '-f', outfile, '-N', '']
        # TODO: Submit SSH public key via API
        # requests.post(api_url, ...), if status == 200, ...
        # TODO: receive Slave ID, save to config
        pass
    
    def cmd_unregister(self):
        # TODO: Sent request to disable this slave, via API
        # requests.post(...)
        pass
    
    def cmd_destroy_vm(self, uuid):
        # TODO: Destroy VM
        # (pids, kill 'em all!, ...)
        pass
    
    def cmd_create_vm(self, uuid):
        # TODO: Create new VM
        # TODO: use webvm_test.sh, collect pids
        pass
    
    

def main(args):
    slave = WebVMClient(url=args.api_url)
    
    print 'API: %s' % url
    
    
    return 0

def run():
    parser = argparse.ArgumentParser(
        description='WebVM Slave Client',
    )
    parser.add_argument('--api-url', dest='api_url', help='API URL', default=WEBVM_API_URL)
    parser.add_argument('-u', '--username', dest='username', help='API username')
    parser.add_argument('-p', '--password', dest='password', help='API password')
    parser.add_argument('command')
    
    args = parser.parse_args()
    sys.exit(main(args))

if __name__ == "__main__":
    run()
