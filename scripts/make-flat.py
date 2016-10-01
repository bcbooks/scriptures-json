#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Quick script that takes an original JSON file and exports a flat edition
# Expects the original JSON to be in the same directory

VERSION = 1

import datetime
import json
import sys

if len(sys.argv) != 2:
    print("Usage: python make-flat.py book-of-mormon.json")
    sys.exit(-1)

filename = sys.argv[1]
output_filename = filename.replace('.json', '')

with open(filename, 'r') as f:
    data = f.read()

data = json.loads(data)

verses = []
headings = []

# Everything but D&C
if 'books' in data:
    for b in data['books']:
        if 'heading' in b:
            headings.append({
                'text': b['heading'],
                'reference': b['book'],
            })

        for c in b['chapters']:
            if 'heading' in c:
                headings.append({
                    'text': c['heading'],
                    'reference': c['reference'],
                })

            for v in c['verses']:
                verses.append({
                    'text': v['text'],
                    'reference': v['reference'],
                })

# D&C
if 'sections' in data:
    for s in data['sections']:
        for v in s['verses']:
            verses.append({
                'text': v['text'],
                'reference': v['reference'],
            })


data = {
    'headings': headings,
    'last_modified': datetime.datetime.now().isoformat()[:10],
    'verses': verses,
    'version': VERSION,
}

with open('{}-flat.json'.format(output_filename), 'w', encoding='utf-8') as f:
    json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)
