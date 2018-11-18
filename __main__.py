
#pip install pymongo

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts> py -m pip install pymongo
import csv
from pymongo import MongoClient

# def todo():
#     conn = MongoClient()
#     print("Connected successfully!!!")
#     db = conn["Proyecto"]
#     colleccion = db["peliculas"]
#     contador_ratings = 0
#     contador_titulos = 0
#     lista = []
#     tira = {}
#     with open('C:/Users/julia/Desktop/IMDB DataSets/titleData.tsv',encoding="utf8") as tsvfile:
#         reader = csv.reader(tsvfile, delimiter='\t')
#         for row in reader:
#             contador_titulos = contador_titulos + 1
#             contador_ratings = 0
#             if contador_titulos>1000000:
#                 break
#                 pass
#             with open('C:/Users/julia/Desktop/IMDB DataSets/ratingsData.tsv', encoding="utf8") as tsvfile2:
#                 reader2 = csv.reader(tsvfile2, delimiter='\t')
#                 for row2 in reader2:
#                     contador_ratings = contador_ratings + 1;
#                     if row2[0]==row[0]:
#                         tira["_id"] = row[0]
#                         tira["tipo"] = row[1]
#                         tira["titulo"] = row[2]
#                         if row[4]==1:
#                             tira["adultos"] = True
#                         else:
#                             tira["adultos"]=False
#                         tira["fechaLanzamiento"] = int(float(row[5]))
#                         tira["fechaFinalizada"] = row[6]
#                         tira["duracion"] = row[7]
#                         tira["generos"] = row[8]
#                         tira["rating"] = float(row2[1])
#                         tira["votacion"] = int(row2[2])
#                         print(tira)
#                         x = colleccion.insert_one(tira)
#                         print("INSERTO: "+x.inserted_id)
#                         lista.append(tira)
#                         break
#                     if contador_ratings > contador_titulos:
#                         break
#
#     return lista
def actualiza_titulos(col):
    tira = {}
    i=1
    with open('C:/Users/julia/Desktop/IMDB DataSets/titleData.tsv',encoding="utf8") as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            if row:
                if len(row)>2:
                    if i != 1:
                        tira["tipo"] = row[1]
                        tira["titulo"] = row[2]
                        if row[4]==1:
                            tira["adultos"] = True
                        else:
                            tira["adultos"] = False
                        if row[5]=="\\N":
                            tira["fechaLanzamiento"] = "Desconocida"
                        else:
                            tira["fechaLanzamiento"] = int(float(row[5]))
                        if row[6]=="\\N":
                            tira["fechaFinalizada"] = "Desconocida"
                        else:
                            tira["fechaFinalizada"] = int(float(row[6]))
                        if row[7]=="\\N":
                            tira["duracion"] = "Desconocida"
                        else:
                            tira["duracion"] = int(float(row[7]))
                        if row[8]=="\\N":
                            tira["generos"] = "Desconocida"
                        else:
                            tira["generos"] = row[8]

                        nuevos = {"$set":tira}
                        col.update_one({"_id":row[0]},nuevos)
                        print(i)
                        i = i + 1
                    else:
                        i=i+1



def inserta_ratings_titulos(colec):
    json ={}
    i = 1
    with open('C:/Users/julia/Desktop/IMDB DataSets/ratingsData.tsv', encoding="utf8") as tsvfile:
        archivo = csv.reader(tsvfile, delimiter='\t')
        for fila in archivo:
            if i!=1:
                json["_id"]=fila[0]
                json["calificacion"]=float(fila[1])
                json["votos"]=int(float(fila[2]))
                x = colec.insert_one(json)
                print("INSERTO: "+x.inserted_id)
            else:
                i = i + 1










try:
    conn = MongoClient()
    print("Conexion Exitosa!!!")
    db = conn["Proyecto"]
    colTitulos = db["titulos"]
    res = colTitulos.find_one()
    cantidad = len(res)
    if cantidad < 1 and cantidad != None:
        inserta_ratings(colTitulos)
    else:
        actualiza_titulos(colTitulos)





except Exception as ex:
    print("Could not connect to MongoDB")
    print(ex)



# def tcons_ratings():
#     lista = []
#     with open('C:/Users/julia/Desktop/IMDB DataSets/ratingsData.tsv', encoding="utf8") as tsvfile:
#         reader = csv.reader(tsvfile, delimiter='\t')
#         for row in reader:
#             lista.append(row[0])
#             lista.append(row[1])
#             lista.append(row[2])
#     return lista
#
# def prueba():
#     contador_ratings = 0
#     contador_titulos = 0
#     lista_tcons_ratings = []
#     lista_tcons_title = []
#     lista_mismos_tconst = []
#     lista_tcons_ratings = tcons_ratings()
#     lista_tcons_title = tcons_title()
#     print(lista_tcons_title)
#     # for valor_title in lista_tcons_title:
#     #     contador_titulos = contador_titulos + 1
#     #     contador_ratings = 0
#     #     for valor_rating in lista_tcons_ratings[contador_titulos]:
#     #         print("Rating: "+valor_rating+"/Titulo: "+valor_title)
#     #         contador_ratings= contador_ratings + 1
#     #         if valor_rating == valor_title:
#     #             print("IGUALES")
#     #             lista_mismos_tconst.append(valor_rating)
#     #             break;
#     #         if contador_ratings>contador_titulos:
#     #             break;
#     # return lista_mismos_tconst
#

# prueba()
