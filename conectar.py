from pymongo import MongoClient
import csv
Client = MongoClient()
db = Client["dbIMDB"]
collection = db["shorts"]
with open('titulos.tsv', encoding="utf8") as tsvfile:
	reader = csv.reader(tsvfile, delimiter='\t')
	for row in reader:
			if str(row[1]) in "short":
				short = {}
				short["code"] = str(row[0])
				short["category"] = str(row[1])
				short["title"] = str(row[2])
				short["year"] = str(row[5])
				if str(row[8]) not in "\\N":
					short["categories"] = str(row[8])
				collection.insert_one(short)
