import pickle
import pandas as pd
import argparse 

class Extractor: 
  def __init__(self):
    pass 


def main(): 
    parser = argparse.ArgumentParser(description = 'Script to extract data from YouTube using the YouTube Data API. This script will require that you provide your own API_KEY.') 
    parser.add_argument('-json_file', type=str, default='./data/youtube_video_results.json', help='path to the json file that contains the scrapped data from YouTube')
    parser.add_argument('')

if __name__ == '__main__': 
  main() 


