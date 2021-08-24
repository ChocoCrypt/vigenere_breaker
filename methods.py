import numpy as np


def IC(c):
    n = len(c)
    alphabet = [chr(i) for i in range(ord("A") , ord("Z")+1)]
    freqs = {ch: 0 for ch in alphabet}
    for ch in c:
        freqs[ch] += 1
    res = 0
    for ch in freqs:
        res += (freqs[ch]*freqs[ch]-1)
    res /= (n*(n-1))
    return res


#este metodo retorna la longitud de un chunk, es util para tener el índice de coindicencia de un chunk
def len_del_chunk(subchunk):
    len_del_chunk = len(subchunk[0])
    return(len_del_chunk)


#este método retorna la media de los índices de coincidencia del tamaño de los posibles chunks para poder saber el tamaño de la llave
def get_ic_subchunk(subchunk):
    len_chunk = len_del_chunk(subchunk)
    sub_strings = ["" for x in range(len_chunk)]
    for i in range(0, len(subchunk)):
        for j in range(len_chunk):
            try:
                sub_strings[j] += subchunk[i][j]
            except:
                pass
    ics = [IC(i) for i in sub_strings] #hay que cambiar la función
    return(np.mean(ics))


def get_key_lenght_text(string):
    len_sub_chunk = 1
    all_sub_chunks = []
    #genero todas las posibles matrices de longitud 0 hasta la longitud del string/2 (suponiendo que la llave no puede ser del tamaño de la mitad del tamaño del string codificado)
    while(len_sub_chunk < len(string)/2):
        sub_chunk = []
        for i in range( 0 , len(string) , len_sub_chunk):
            sub_string = string[i:i+len_sub_chunk]
            sub_chunk.append(sub_string)
        all_sub_chunks.append(sub_chunk)
        len_sub_chunk += 1
    english_index_of_coincidence = 0.065
    #agarro el chunk que mas se parece a los indices de coincidencia originales, así se la longitud de la llave , la cuál guardo en la variable mini
    proms = [np.abs(english_index_of_coincidence -get_ic_subchunk(i)) for i in all_sub_chunks]
    mini = np.argmin(proms) +1
    #genero unas palabras vacías para posteriormente llenarlas de la forma de la matriz
    letters = ["" for x in range(mini)]
    for j in range(mini):
        for i in range(len(string)):
            if(i%mini == j):
                letters[i%mini] += string[i]
    #retorno la matriz de n letras de longitud de la llave
    return(letters)


#este método calcula la distancia euclideana la frecuencia de caracteres de una palabra al inglés
def distance_to_english(string):
    alfabeto = [chr(i) for i in range(ord("A") , ord("Z")+1)]
    #frecuencia de caracteres dada por válerie
    english_freqs = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001]
    frequences = {i:0 for i in alfabeto}
    for i in string:
        frequences[i] += 1
    #normalizamos las frecuencias
    for i in frequences:
        frequences[i] = frequences[i]/len(frequences)
    distance = 0
    #formula distancia euclideana
    for i in range(len(frequences.values())):
        x = list(frequences.values())[i]
        y = english_freqs[i]
        distance += (x-y)*(x-y)
    distance = np.sqrt(distance)
    return(distance)


#defino hacerle un shift a una palabra para medir las distancias de los shifts
def shift(string, n):
    alfabeto = [chr(i) for i in range(ord("A") , ord("Z")+1)]
    newstring = ""
    for i in string:
        new_letter = alfabeto[(alfabeto.index(i) + n)%26]
        newstring += new_letter
    return(newstring)


#recibo un string, genero los 26 shifts posibles y le hago el shift al más cercano al inglés
def shif_string_to_decoded_string(string):
    distances = []
    for i in range(26):
        distance = distance_to_english(shift(string , i))
        distances.append(distance)
    min_distance = np.argmin(distances)
    decoded_string = shift(string , min_distance)
    return(decoded_string)


#recibo una lista de sub strings de longitud de la llave y a todos les hago el shift al inglés
def adecuated_string_to_decoded_strings(adecuated_string):
    new_pals = []
    for i in adecuated_string:
        pal = shif_string_to_decoded_string(i)
        new_pals.append(pal)
    return(new_pals)


#recibo una lista de chunks ya en inglés y los concateno, retorno la concatenación
def reverse_decoded_strings(decoded_strings):
    tam = len(decoded_strings[0])
    pegado = "".join(decoded_strings)
    pals = ["" for x in range(tam)]
    index = 1
    for j in range(tam):
        for i in range(len(pegado)):
            if(i%tam == j):
                pals[i%tam] += pegado[i]
    final_decode ="".join(pals)
    return(final_decode)
