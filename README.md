# Youtube Recommendation Engine 
A YouTube Video Recommendation Engine using video title and video description of YouTube Video based on Cosine Similarity to understand content based filtering. 

## Concept Overview  
Content Based Filtering is a popular recommendation technique that is used to collect a unique user's preference given the characteristics of the items and the preferences of the users. These items are represented using a set of features depending on the type of items that are being recommended. In this particular case, the items given are Youtube videos that pertain to the user's preference. The features that can help us best understand the user's behaviour with YouTube are the characteristics of the video, namely the title, description as well as the author of the video. Using this given information, this repo, aims at building a mini recommendation engine by comparing the items with the highest similarity scores. 

## Repository Structure 
**data** - contains all the necessary data files, including the data scrapped from youtube using the YouTube Data API, the different search queries used as templates for scrapping etc. 

**scripts** - contains all the scripts for scrapping, cleaning and processing data as well as the construction of the CBF. 



