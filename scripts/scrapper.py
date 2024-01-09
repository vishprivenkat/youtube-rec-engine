from googleapiclient.discovery import build
import argparse 
import json 


class CollectYoutubeData: 
    def __init__(self, api_key): 
        self.topics = []  
        self.results = [] 
        self.output_file_path = './youtube_video_results.json'
        self.API_KEY = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.API_KEY)

    def search_youtube(self, query, max_results=50):
        if len(self.API_KEY) > 0: 
            
            request = self.youtube.search().list(
                q=query, 
                part='snippet',
                type='video', 
                maxResults = max_results
            )
            try: 
                response = request.execute()
                video_info = []
                for item in response['items']:
                    video_id = item['id']['videoId']
                    video_title = item['snippet']['title']
                    video_description = item['snippet']['description']
                    video_info.append({'search_query': query, 'video_id': video_id, 'video_title': video_title, 'video_description': video_description})

                return video_info 
            except Exception as e: 
                return None 
        return None 

    def search_youtube_video(self, video_id):
        if len(video_id) > 0: 
            request = self.youtube.videos().list(
                    part='snippet',
                    id=video_id
                ) 
            try: 
                response = request.execute() 
                if 'items' in response and response['items']: 
                    video_info = response['items'][0]['snippet']
                    video_title = video_info['title'] 
                    video_description = video_info['description'] 

                    return video_title, video_description 
                else: 
                    return None, None 

            except Exception as e: 
                print(f"Error in Fetching Video Information: {str(e)}") 
                return None, None 
        else:
            return None, None  


    def get_topics(self, topics_file_path): 
        with open(topics_file_path, 'r') as file: 
            for line in file: 
                self.topics.append(line.strip()) 
    
    def collect_results(self, max_results= 50): 
        for topic in self.topics: 
            result = self.search_youtube(topic, max_results)
            self.results+= result if result else {} 

        
    
    def save_results_json(self, output_file_path): 
        with open(output_file_path, 'w') as json_file: 
            json.dump(self.results, json_file, indent = 2) 
        
        print('Search Results have been saved successfully.')
        

def main(): 
    parser = argparse.ArgumentParser(description = 'Script to extract data from YouTube using the YouTube Data API. This script will require that you provide your own API_KEY.') 
    parser.add_argument('-topics_file', type=str, default='./topics.txt', help='path to the file that contains the topics for searching') 
    parser.add_argument('-output_json', type=str, default='./youtube_video_results.json', help = 'path to the file that contains the resultant data scrapped from YouTube') 
    parser.add_argument('-max_search_results', type=int, default=50, help='Number of search results required per search query') 
    parser.add_argument('-API_KEY', type=str, required=True, help='Give your YouTube Data API key' ) 

    args = parser.parse_args() 

    scrapper = CollectYoutubeData(args.API_KEY)  

    scrapper.get_topics(args.topics_file) 
    scrapper.collect_results(max_results=args.max_search_results) 
    scrapper.save_results_json(args.output_json) 

 
if __name__ == '__main__':
    main() 



