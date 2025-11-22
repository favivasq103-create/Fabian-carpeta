meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "reirse",
            "IDK": "yo no se",
            "HACER EL OSO": "pasar pena"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(word)
else:
    print("esta palabra no se encuentra en este diccionario :c")
