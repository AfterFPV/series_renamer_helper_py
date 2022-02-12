#!/usr/bin/env python3

import sys
import os
from os import path
#import pandas as pd
#import wikipedia as wp


def get_args():
    series_name = input("Series Name:" )
    season_num = input("Season Number: ")
    series_path = input("Series Path: ")
    series_ext = input("Series File Extension: ")
    series_url = input("Wikipedia URL: ")

    print()

    return series_name, season_num, series_path, series_ext, series_url


def test_args():
    series_name = "Squid Game"
    season_num = 1
    series_path = "./Squid.Game.S01.DUBBED.WEBRip.x265-ION265"
    series_ext = "mp4"
    series_url = "https://en.wikipedia.org/wiki/Squid_Game"

    return series_name, season_num, series_path, series_ext, series_url


def main():
    print("Welcome to the TV Series Batch Renamer")

    series_name, season_num, series_path, series_ext, series_url = get_args()
    series_name, season_num, series_path, series_ext, series_url = test_args()
    
    if not path.exists(series_path):
        sys.exit("Series Path INVALID")

    files = os.listdir(series_path)
    for file in files:
        if os.path.isfile(os.path.join(series_path, file)):
            print(file)

    print(series_name)
    print(series_url)



if __name__ == "__main__":
    main()









