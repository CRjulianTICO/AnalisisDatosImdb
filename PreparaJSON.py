from PreparaData import PreparaData

class PreparaJson:

    list_tconst_title = None
    list_title_data = None
    list_tconst_ratings = None
    list_ratings_data = None
    pd = None

    def __init__(self):
        self.list_tconst_title = []
        self.list_title_data = []
        self.list_tconst_ratings = []
        self.list_ratings_data = []
        self.pd = PreparaData()

    def json_pelicula_rating(self):
        json = []
        tira = {}
        self.list_title_data = self.pd.title_data()
        self.list_ratings_data = self.pd.ratings_data()
        for title_data in self.list_title_data:
            for rating_data in self.list_ratings_data:
                tconst_title = str(title_data[[title_data.columns[0]]])
                tconst_rating = str(rating_data[[rating_data.columns[0]]])
                if tconst_title==tconst_rating:
                    print('IGUALES\n'+'TITLE: '+tconst_title+'**RATING: '+tconst_rating)
                    tira["_id"] = title_data[[title_data.columns[0]]]
                    tira["tipo"] = title_data[[title_data.columns[1]]]
                    tira["titulo"] = title_data[[title_data.columns[2]]]
                    tira["fecha"] = title_data[[title_data.columns[5]]]
                    tira["generos"] = title_data[[title_data.columns[8]]]
                    tira["rating"] = rating_data[[rating_data.columns[1]]]
                    tira["votos"] = rating_data[[rating_data.columns[2]]]
                    print("TIRA:"+tira)
                    json.append(tira)
                else:
                    print('nop')
                    print('DIFERENTES\n'+'TITLE: '+tconst_title+'**RATING: '+tconst_rating)


        print(json)



        # for titleData in self.list_tconst_ratings:
        #     print(titleData[[titleData.columns[0],titleData.columns[1],titleData.columns[2]]])
