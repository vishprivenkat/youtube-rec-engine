import pafy
import pickle
import pandas as pd

file = open('links.pickle','rb')
links = pickle.load(file)
file.close()

dataset = pd.DataFrame(columns = ["link","title","category","author"])

i = 1
count_couldnt_collect = 0
for link in links:
    try:
        video = pafy.new(link)
        dataset = dataset.append({"link":link, "title":video.title, "category":video.category, "author":video.author}, ignore_index=True)
        print("*", end=" ")
        i+=1
    except Exception as e:
        count_couldnt_collect+=1
        print("Skipping to the next Video")

dataset.to_csv('base_data.csv')