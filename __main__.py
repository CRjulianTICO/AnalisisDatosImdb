
#pip install pymongo

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts> py -m pip install pymongo

from PreparaJSON import PreparaJson
from pymongo import MongoClient
pj = PreparaJson()

pj.json_pelicula_rating()


try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")
