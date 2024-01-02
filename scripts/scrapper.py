from googleapiclient.discovery import build
import argparse 
import json 

api_key = 'YOUR_API_KEY'
youtube = build('youtube', 'v3', developerKey=api_key)

class CollectYoutubeData: 
    def __init__(self): 
        self.topics = []  
        self.results = [] 
        self.output_file_path = './youtube_video_results.json'

    def search_youtube(self, query, max_results=50):
        request = youtube.search().list(
            q=query, 
            part='snippet',
            type='video', 
            maxResults = max_results
        )
        response = request.execute()
        video_info = []
        for item in response['items']:
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_description = item['snippet']['description']
            video_info.append({'search_query': query, 'video_id': video_id, 'video_title': video_title, 'video_description': video_description})

        return video_info 

    def get_topics(self, topics_file_path): 
        with open(topics_file_path, 'r') as file: 
            for line in file: 
                self.topics.append(line.strip()) 
    
    def collect_results(self, max_results= 50): 
        for topic in self.topics: 
            self.results+=self.search_youtube(topic, max_results)
        
    
    def save_results_json(self, output_file_path): 
        with open(output_file_path, 'w') as json_file: 
            json.dump(self.results, json_file, indent = 2) 
        
        print('Search Results have been saved successfully.')
        

def main(): 
    parser = argparse.ArgumentParser(description = 'Script to extract data from YouTube using the YouTube Data API. This script will require that you provide your own API_KEY.') 
    parser.add_argument('-topics_file', type=str, default='./topics.txt', help='path to the file that contains the topics for searching') 
    parser.add_argument('-output_json', type=str, default='./youtube_video_results.json', help = 'path to the file that contains the resultant data scrapped from YouTube') 
    parser.add_argument('-max_search_results', type=int, default=50, help='Number of search results required per search query') 

    args = parser.parse_args() 

    scrapper = CollectYoutubeData()  

    scrapper.get_topics(args.topics_file) 
    scrapper.collect_results(max_results=args.max_search_results) 
    scrapper.save_results_json(args.output_json) 

 





if __name__ == '__main__':
    main() 



