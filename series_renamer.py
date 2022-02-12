#!/usr/bin/env python3

import sys
import os
from os import path

print("Welcome to the TV Series Batch Renamer")


series_name = input("Series Name:" )
season_num = input("Season Number: ")
series_path = input("Series Path: ")
series_ext = input("Series File Extension: ")
series_url = input("Wikipedia URL: ")

print()


if not path.exists(series_path):
    sys.exit("Series Path INVALID")

files = os.listdir(series_path)
for file in files:
    if os.path.isfile(os.path.join(series_path, file)):
        print(file)

print(series)
print(url)
