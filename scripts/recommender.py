import json
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessor import Preprocessor 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import argparse 



class Recommender: 
  def __init__(self): 
    self.preprocessor = Preprocessor() 
    self.vectorizer = TfidfVectorizer()

  def preprocess_text(self, text):  
    formatted_text = self.preprocessor.format_string(text) 
    return self.preprocessor.remove_stop_words(formatted_text)
  
  def get_tfidf_vector(self, processed_text):
    tfidf_vector = self.vectorizer.fit_transform([processed_text]).toarray()[0]
    return tfidf_vector

  def stream_and_process_data(self, json_file_path, chunk_size = 1000):  
    
    self.documents = {} 
    with open(json_file_path, 'r', encodings='utf-8') as file: 
      while True: 
        lines = [file.readline().strip() for _ in range(chunk_size)] 
        if not any(lines): 
          break 
        for line in lines: 
          document = json.loads(line) 
          text = document.get('video_title', '') + ' ' + document.get('video_description', '')
          processed_text = self.preprocess_text(text)
          self.documents[document['video_id']] = self.get_tfidf_vector(processed_text)  
    
  
  def find_top_similar_videos(self, query_URL, top_n=5): 
    query_vector = self.preprocessor.extract_video_id(query_URL) 
    if query_vector: 
      similarities = {} 
      for video_id, vector in self.documents.items(): 
        similarity = cosine_similarity([query_vector], [vector])[0][0] 
        similarities[video_id] = similarity 

      top_similarities = dict(sorted(similarity.items(), key = lambda item: item[1], reverse= True)[:top_n])  
      return top_similarities 
    else: 
      return None 
    
  

def main(): 
  parser = argparse.ArgumentParser(description = 'Script to extract data from YouTube using the YouTube Data API. This script will require that you provide your own API_KEY.') 

if __name__ == '__main__': 
  main() 
    


   
        
