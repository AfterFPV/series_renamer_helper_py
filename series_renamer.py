#!/usr/bin/env python3

import sys
import os
from os import path
import pandas as pd
import wikipedia as wp
import re
import urllib.request



class MySeries:
    def __init__(self, name='', url=''):
        self.series_name = name
        self.series_url = url

    def get_data(self):
        print(f'{self.series_name}+{self.series_url}j')

    def generate_url(self):
        self.series_url = self.series_name.replace(" ", "")
        self.series_url = self.series_url.replace("The", "")
        self.series_url = "http://epguides.com/" + self.series_url



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
    print("")
    print("    * this script generates txt files of episode names associated with S01E01")
    print("    * these output files are for use by the c script as a lookup table of episode names")
    print("")
    print("")

    
    series_dir = os.path.join('d:\\', r"s2mccaffr", 'Videos', 'Series')
    print("Scanning:", series_dir)

    if not path.exists(series_dir):
        sys.exit("Series Path INVALID")


    series_list = [] 

    files = os.listdir(series_dir)
    for file in files:
        series_list.append(MySeries(file,''))
        #print(file)

    for obj in series_list:
        obj.generate_url()
        #print(obj.series_name)

        try:
            page = urllib.request.urlopen(obj.series_url)
            content = page.read().decode('utf-8')
            links = re.findall('exportToCSVmaze.asp\?maze=[0-9]*', content)
            for link in links:
                print("curl https://epguides.com/common/" + link + " > \"" + obj.series_name + ".txt\"")


        
        except urllib.error.URLError as e:
            print("# " +  e.reason + " - " + obj.series_name)


    
    sys.exit()


    episode_names = scrape_wikipedia(series_url)
    for name in episode_names:
        print(name)



if __name__ == "__main__":
    main()
