#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GPLv3

# (c) 2013 Ville Korhonen <ville@xd.fi>

import os
import sys
import json
import requests
import argparse

WEBVM_API_HOST = 'nm.0xff.fi'
WEBVM_API_VERSION = "v1"
WEBVM_API_PROTO = 'https'
WEBVM_API_BASE = "%(proto)s://%(host)s/api/%(version)s"

# TODO: By default, use HTTPS

def main(args):
    api_url = WEBVM_API_BASE % {
        'proto': WEBVM_API_PROTO,
        'host': args.host,
        'version': WEBVM_API_VERSION,
        
    }
    
    
    
    return 0

def run():
    parser = argparse.ArgumentParser(
        description='WebVM Slave Client',
    )
    parser.add_argument('--host', dest='host', help='API server', default=WEBVM_API_HOST)
    
    args = parser.parse_args()
    sys.exit(main(args))

if __name__ == "__main__":
    run()
