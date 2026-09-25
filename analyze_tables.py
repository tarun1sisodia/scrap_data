import glob
import os
import re
import sys
import json
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob('01a0d897-6996-76f1-8656-c70611d44eb8/*.md')
print(f"Total markdown files found: {len(files)}")

one_way_round_trip = []
day_120km = []
tempo_traveller = []
other_tables = []
no_tables = []

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    basename = os.path.basename(f)
    
    if 'Price (One Way)' in content:
        one_way_round_trip.append((basename, content))
    elif '1 Day / 120 K.M.' in content:
        day_120km.append((basename, content))
    elif 'Tempo Traveller' in content and 'Price / K.M.' in content:
        tempo_traveller.append((basename, content))
    elif '|' in content and '---' in content:
        other_tables.append((basename, content))
    else:
        no_tables.append((basename, content))

print(f"One Way & Round Trip table files: {len(one_way_round_trip)}")
print(f"1 Day / 120 KM table files: {len(day_120km)}")
print(f"Tempo Traveller table files: {len(tempo_traveller)}")
print(f"Other tables: {len(other_tables)}")
print(f"No tables: {len(no_tables)}")

# Inspect unique tables in one_way_round_trip
ow_tables_map = {}
for name, content in one_way_round_trip:
    m = re.search(r'(\| Vehicle Type \| Model \|.*?\n(?:\|.*?\n)+)', content)
    if m:
        tbl = m.group(0).strip()
        ow_tables_map.setdefault(tbl, []).append(name)

print("\n--- DISTINCT ONE WAY / ROUND TRIP TABLES ---")
for tbl, fnames in ow_tables_map.items():
    print(f"Count: {len(fnames)} files")
    print(f"Sample file: {fnames[0]}")
    print(tbl)
    print("-" * 50)

# Inspect unique tables in day_120km
day_tables_map = {}
for name, content in day_120km:
    m = re.search(r'(\| Vehicle Type \| Model \|.*?\n(?:\|.*?\n)+)', content)
    if m:
        tbl = m.group(0).strip()
        day_tables_map.setdefault(tbl, []).append(name)

print("\n--- DISTINCT 1 DAY / 120 KM TABLES ---")
for tbl, fnames in day_tables_map.items():
    print(f"Count: {len(fnames)} files")
    print(f"Sample file: {fnames[0]}")
    print(tbl)
    print("-" * 50)

# Inspect unique tables in tempo_traveller
tempo_tables_map = {}
for name, content in tempo_traveller:
    m = re.search(r'(\| Tempo Traveller \|.*?\n(?:\|.*?\n)+)', content)
    if m:
        tbl = m.group(0).strip()
        tempo_tables_map.setdefault(tbl, []).append(name)

print("\n--- DISTINCT TEMPO TRAVELLER TABLES ---")
for tbl, fnames in tempo_tables_map.items():
    print(f"Count: {len(fnames)} files")
    print(f"Sample file: {fnames[0]}")
    print(tbl)
    print("-" * 50)
