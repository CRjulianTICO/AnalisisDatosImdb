#pip install pandas

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts> py -m pip install --user pandas

#pip install pymongo

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts> py -m pip install pymongo


import pandas as pd
class PreparaData:

    list_tconstTitle = None
    list_titleData = None
    list_tconstRatings = None
    list_ratingsData = None

    def __init__(self):
        self.list_tconstTitle = []
        self.list_titleData = []
        self.list_tconstRatings = []
        self.list_ratingsData = []

    def tconst_TitleData(self):
        search_info = pd.read_csv('C:/Users/julia/Desktop/IMDB DataSets/titleData.tsv',delimiter="\t",nrows=8000000,encoding='utf-8',low_memory=False,error_bad_lines = False,chunksize=150000)#skiprows=1000000,
        for data_set in search_info:
            self.list_tconstTitle.append(data_set[[data_set.columns[0]]])
        return self.list_tconstTitle

    def title_data(self):
        search_title_data = pd.read_csv('C:/Users/julia/Desktop/IMDB DataSets/titleData.tsv',delimiter="\t",nrows=8000000,encoding='utf-8',low_memory=False,error_bad_lines = False,chunksize=150000)#skiprows=1000000,
        # for data_set in search_title_data:
        #     self.list_titleData+=data_set
        self.list_titleData = search_title_data
        return self.list_titleData

    def tconst_RatingsData(self):
        search_tconst_ratings = pd.read_csv('C:/Users/julia/Desktop/IMDB DataSets/ratingsData.tsv',delimiter="\t",nrows=8000000,encoding='utf-8',low_memory=False,error_bad_lines = False,chunksize=150000)
        for data_set in search_tconst_ratings:
            self.list_tconstRatings.append(data_set[[data_set.columns[0]]])
        return self.list_tconstRatings

    def ratings_data(self):
        search_ratings_data = pd.read_csv('C:/Users/julia/Desktop/IMDB DataSets/ratingsData.tsv',delimiter="\t",nrows=8000000,encoding='utf-8',low_memory=False,error_bad_lines = False,chunksize=150000)#skiprows=1000000,
        # for data_set in search_ratings_data:
        #     self.list_ratingsData+=data_set
        self.list_ratingsData = search_ratings_data
        return self.list_ratingsData




    #print(data_set[[data_set.columns[0]]])


#print(list(search_info.columns.values)) #file header
#print(search_info[[search_info.columns[0],search_info.columns[1],search_info.columns[2],search_info.columns[3],search_info.columns[4]]])


#print(search_info.columns[0])
