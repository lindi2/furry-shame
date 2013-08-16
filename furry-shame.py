#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GPLv3

# (c) 2013 Ville Korhonen <ville@xd.fi>

import os
import sys
import json
import requests

WEBVM_API_VERSION = "v1"
WEBVM_API_BASE = "http://%(host)s/api/%(version)s"

def main(args):
    api_url = WEBVM_API_BASE % {
        'host': 'nm.0xff.fi',
        'version': WEBVM_API_VERSION,
    }
    
    
    
    return 0

def run():
    args = []
    sys.exit(main(args))

if __name__ == "__main__":
    run()
