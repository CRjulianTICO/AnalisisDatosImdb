import csv

#conectar python con mongo
#pip install pymongo

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts

#C:\Users\julia\AppData\Roaming\Python\Python37\Scripts> py -m pip install pymongo

from pymongo import MongoClient

#Libreria para el metodo ver_linea_especifica
from itertools import islice




#metodo para ver lineas especificas dentro del csv
def ver_linea_especifica(col):
    print("algo")
    with open('C:/Users/julia/Desktop/IMDB DataSets/titleData.tsv',encoding="utf8") as fd:
        reader=csv.reader(fd, delimiter='\t')
        interestingrows=[row for idx, row in enumerate(reader) if idx in (1,2247794)]
        print(interestingrows)


#este metodo actualiza agrega los titulos que ya estaban insertados por inserta ratings cuando a
#inserta ratings  se le pasa por parametro la misma coleccion que este metodo
def actualiza_titulos(col):
    tira = {}
    i=1
    with open('C:/Users/julia/Desktop/IMDB DataSets/titleData.tsv',encoding="utf8") as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            if row:
                if len(row)>2:
                    if i != 1:
                        if len(row[1])>2:
                            tira["tipo"] = row[1]
                        if len(row[2])>2:
                            tira["titulo"] = row[2]
                        if row[4]==1 and len(row[4])>2:
                            tira["adultos"] = True
                        else:
                            tira["adultos"] = False
                        if row[5]=="\\N":
                            tira["fechaLanzamiento"] = "Desconocida"
                        else:
                            if len(row[5])>2:
                                tira["fechaLanzamiento"] = int(float(row[5]))
                        if row[6]=="\\N":
                            tira["fechaFinalizada"] = "Desconocida"
                        else:
                            if len(row[6])>2:
                                tira["fechaFinalizada"] = int(float(row[6]))
                        if row[7]=="\\N":
                            tira["duracion"] = "Desconocida"
                        else:
                            if len(row[7])>2:
                                tira["duracion"] = int(float(row[7]))
                        if row[8]=="\\N":
                            tira["generos"] = "Desconocida"
                        else:
                            if len(row[8])>2:
                                tira["generos"] = row[8]

                        nuevos = {"$set":tira}
                        if len(row[0])>2:
                            col.update_one({"_id":row[0]},nuevos)
                            print(i)
                            i = i + 1
                    else:
                        i=i+1




#metodo para empezar a insertar desde una linea especifica en este es un ejemplo con titulos
def insertar_desde_linea_especifica(col):
    tira = {}
    i=4726446
    with open('C:/Users/julia/Desktop/IMDB DataSets/titleData.tsv',encoding="utf8") as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in islice(reader,4726446,None):
            if row:
                if len(row)>2:
                    if i != 1:
                        if len(row[1])>2:
                            tira["tipo"] = row[1]
                        if len(row[2])>2:
                            tira["titulo"] = row[2]
                        if row[4]==1 and len(row[4])>2:
                            tira["adultos"] = True
                        else:
                            tira["adultos"] = False
                        if row[5]=="\\N":
                            tira["fechaLanzamiento"] = "Desconocida"
                        else:
                            if len(row[5])>2:
                                tira["fechaLanzamiento"] = int(float(row[5]))
                        if row[6]=="\\N":
                            tira["fechaFinalizada"] = "Desconocida"
                        else:
                            if len(row[6])>2:
                                tira["fechaFinalizada"] = int(float(row[6]))
                        if row[7]=="\\N":
                            tira["duracion"] = "Desconocida"
                        else:
                            if len(row[7])>2:
                                tira["duracion"] = int(float(row[7]))
                        if row[8]=="\\N":
                            tira["generos"] = "Desconocida"
                        else:
                            if len(row[8])>2:
                                tira["generos"] = row[8]

                        nuevos = {"$set":tira}
                        if len(row[0])>2:
                            col.update_one({"_id":row[0]},nuevos)
                            print(i)
                            i = i + 1
                    else:
                        i=i+1


#Metodo para actualizar los rankings para ponerle la informacion mas relevante de los titulos
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



def inserta_ratings(col):
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



def inserta_crews(col):
    json ={}
    i = 1
    with open('C:/Users/julia/Desktop/IMDB DataSets/crewData.tsv', encoding="utf8") as tsvfile:
        archivo = csv.reader(tsvfile, delimiter='\t')
        for fila in archivo:
            if i!=1:
                json["_id"] = i
                json["id_titulo"] =fila[0]
                if fila[1]=="\\N":
                    json["directores"] = "Desconocido"
                else:
                    json["directores"] = fila[1]
                if fila[2]=="\\N":
                    json["escritores"] = "Desconocido"
                else:
                    json["escritores"] = fila[2]
                res = col.insert_one(json)
            print("INSERTO: "+res.inserted_id+"/"+fila[0])
            i = i + 1
        else:
            i = i + 1


def inserta_episodes(col):
    json ={}
    i = 1
    with open('C:/Users/julia/Desktop/IMDB DataSets/espisodeData.tsv', encoding="utf8") as tsvfile:
        archivo = csv.reader(tsvfile, delimiter='\t')
        for fila in archivo:
            if i!=1:
                json["_id"] = fila[0]
                json["id_padre"] = fila[1]
                if fila[2]=="\\N":
                    json["numeroTemporada"] = "Desconocida"
                else:
                    json["numeroTemporada"] = int(float(fila[2]))
                if fila[3]=="\\N":
                    json["numeroEpisodio"] = "Desconocido"
                else:
                    json["numeroEpisodio"] = int(float(fila[3]))
                res = col.insert_one(json)
            print("INSERTO: "+res.inserted_id+"/"+fila[0])
            i = i + 1
        else:
            i = i + 1



def inserta_names(col):
    json ={}
    i = 1
    with open('C:/Users/julia/Desktop/IMDB DataSets/nameData.tsv', encoding="utf8") as tsvfile:
        archivo = csv.reader(tsvfile, delimiter='\t')
        for fila in archivo:
            if i!=1:
                json["_id"] = fila[0]
                json["nombre"] = fila[1]
                if fila[2]:
                    if len(fila[2])>2:
                        if fila[2]=="\\N":
                            json["fechaNacimiento"] = "Desconocida"
                        else:
                            json["fechaNacimiento"] = int(float(fila[2]))
                if fila[3]:
                    if len(fila[3])>2:
                        if fila[3]=="\\N":
                            json["fechaMuerte"] = "Desconocido"
                        else:
                            json["fechaMuerte"] = int(float(fila[3]))
                if fila[4]:
                    if len(fila[4])>2:
                        if fila[4]=="\\N":
                            json["profesiones"] = "Desconocido"
                        else:
                            json["profesiones"] = fila[4]
                if fila[5]:
                    if len(fila[5])>2:
                        if fila[5]=="\\N":
                            json["titulos"] = "Desconocido"
                        else:
                            json["titulos"] = fila[5]
                res = col.insert_one(json)
            print("INSERTO: "+res.inserted_id+"/"+fila[0])
            i = i + 1
        else:
            i = i + 1




#Aqui se ejecuta todo el codigo que lee y guarda en la base de datos
try:
    conn = MongoClient()
    print("Conexion Exitosa!!!")
    db = conn["Proyecto"]
    col_titulos = db["titulos"]
    col_nombres = db["nombres"]
    col_equipos = db["equipo"]
    col_episodios = db["episodios"]
    col_calificaciones = db["calificacion"]
    inserta_ratings_titulos(col_titulos)
    actualiza_titulos(col_titulos)
    inserta_ratings(col_calificaciones)
    inserta_names(col_nombres)
    inserta_episodes(col_episodios)
    inserta_crews(col_equipos)


except Exception as ex:
    print("Could not connect to MongoDB")
    print(ex)
