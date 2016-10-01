#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Quick script that takes an original JSON file and exports a reference edition
# Expects the original JSON to be in the same directory

VERSION = 1

from collections import OrderedDict
import datetime
import json
import sys

if len(sys.argv) != 2:
    print("Usage: python make-reference.py book-of-mormon.json")
    sys.exit(-1)

filename = sys.argv[1]
output_filename = filename.replace('.json', '')

with open(filename, 'r') as f:
    data = f.read()

data = json.loads(data)

output = OrderedDict()

# Everything but D&C
if 'books' in data:
    for b in data['books']:
        book = b['book']
        if book not in output:
            output[book] = OrderedDict()

        if 'heading' in b:
            output[book]['heading'] = b['heading']

        for c in b['chapters']:
            chapter = str(c['chapter'])

            if chapter not in output[book]:
                output[book][chapter] = OrderedDict()

            if 'heading' in c:
                output[book][chapter]['heading'] = c['heading']

            for v in c['verses']:
                output[book][chapter][str(v['verse'])] = v['text']

# D&C
if 'sections' in data:
    for s in data['sections']:
        section = str(s['section'])

        if section not in output:
            output[section] = OrderedDict()

        for v in s['verses']:
            output[section][str(v['verse'])] = v['text']

output['last_modified'] = datetime.datetime.now().isoformat()[:10]
output['version'] = VERSION

with open('{}-reference.json'.format(output_filename), 'w', encoding='utf-8') as f:
    json.dump(output, f, sort_keys=False, indent=4, ensure_ascii=False)
