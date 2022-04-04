#!/usr/bin/env python3

import sys
import os
from os import path
import pandas as pd
import wikipedia as wp
import re



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
    series_url = "Squid_Game#Episodes"

    return series_name, season_num, series_path, series_ext, series_url


def scrape_wikipedia(series_url):
    html = wp.page(series_url).html().encode("UTF-8")
    try: 
        df = pd.read_html(html)[1]
    except IndexError:
        df = pd.read_html(html)[0]
    #print(df.to_string())

    episode_names = []
    bitflip = True
    for index, row in df.iterrows():
        if (bitflip):
            name = re.findall('"([^"]*)"', row[1])[0]
            episode_names.append(name)
            bitflip = False
        else:
            bitflip = True
    
    return episode_names



def main():
    print("Welcome to the TV Series Batch Renamer")

    #setup
    #series_name, season_num, series_path, series_ext, series_url = get_args()
    series_name, season_num, series_path, series_ext, series_url = test_args()

    #get table from wikipedia
    episode_names = scrape_wikipedia(series_url)
    for name in episode_names:
        print(name)

    #find local series files
    if not path.exists(series_path):
        sys.exit("Series Path INVALID")

    files = os.listdir(series_path)
    #for file in files:
     #   if os.path.isfile(os.path.join(series_path, file)):
            #print(file)

    #print(series_name)
    #print(series_url)



if __name__ == "__main__":
    main()