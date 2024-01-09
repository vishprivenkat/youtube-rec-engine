import pandas as pd
import numpy as numpy
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words("english"))


class Preprocessor: 
    def __init__(self):
        pass 
        
    def format_string(self, sentence): 
        """
        Removes all the special characters from a sentence retaining only alphanumeric characters 
        """
        pattern = r'[^a-zA-Z0-9\s]'
        return ' '.join(set(re.sub(pattern, '', sentence).lower()))

    def remove_stop_words(self, sentence): 
        """
        Tokenizes a sentence and then removes the stopwords by checking if the word is a part of the stopwords corpus. 
        """
        words = word_tokenize(sentence) 
        filtered_words = [ word for word in words if word not in stop_words] 
        return ' '.join(filtered_words) 

    def extract_video_id(self, youtube_URL): 
        """
        Takes a URL and checks the validity of a YouTube link. If its a valid link, then the video ID is extracted out. 
        """
        pattern = re.compile(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
        match = pattern.search(youtube_URL)
        return match.group(1) if match else None
    
    

    