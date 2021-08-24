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


def ic(string):
    ic = 0
    leng_text = len(string)
    alfabeto = [chr(i) for i in range(ord("A") , ord("Z")+1)]
    frecuencias = {char:0 for char in alfabeto}
    for i in string:
        frecuencias[i] += 1
    for i in frecuencias:
        ic += (frecuencias[i]*(frecuencias[i]-1))
    ic = ic/(leng_text*(leng_text-1))
    return(ic)



def len_del_chunk(subchunk):
    len_del_chunk = len(subchunk[0])
    return(len_del_chunk)


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
    while(len_sub_chunk < len(string)/2):
        sub_chunk = []
        for i in range( 0 , len(string) , len_sub_chunk):
            sub_string = string[i:i+len_sub_chunk]
            sub_chunk.append(sub_string)
        all_sub_chunks.append(sub_chunk)
        len_sub_chunk += 1
    english_index_of_coincidence = 0.065
    proms = [np.abs(english_index_of_coincidence -get_ic_subchunk(i)) for i in all_sub_chunks]
    mini = np.argmin(proms) +1
    adecuated_strings = all_sub_chunks[len(string)//mini-1]
    index = 0
    letters = ["" for x in range(mini)]
    for j in range(mini):
        for i in range(len(string)):
            if(i%mini == j):
                letters[i%mini] += string[i]

    return(adecuated_strings)

def distance_to_english(string):
    alfabeto = [chr(i) for i in range(ord("A") , ord("Z")+1)]
    distance = 0
    english_freqs = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001]
    frequences = {i:0 for i in alfabeto}
    for i in string:
        frequences[i] += 1
    for i in frequences:
        frequences[i]/=len(string)
    for i in range(len(frequences)):
        distance+=((list(frequences.values())[i]-english_freqs[i])**2)
    distance = np.sqrt(distance)
    return(distance)

def shift(string, n):
    alfabeto = [chr(i) for i in range(ord("A") , ord("Z")+1)]
    newstring = ""
    for i in string:
        new_letter = alfabeto[(alfabeto.index(i) + n)%26]
        newstring += new_letter
    return(newstring)


def distance_to_english_adecuated_string(adecuated_string):
    alfabeto = [chr(i) for i in range(ord("A") , ord("Z")+1)]
    for i in adecuated_string:
        distances = []
        for j in range(26):
            newpal = shift(i,j)
            distance = distance_to_english(newpal)
            distances.append(distance)
        print(np.min(distances))
        min_distance = np.argmin(distances)
        new_pal = shift(i , min_distance)




strings = get_key_lenght_text("REIAUBLZXYQOKHMRNTEZHFLVIABHDMJMSJOGIRETPHBVVFTQHEXTARVIXSNQRIQPEJOLMDDEJORGVFECUTQVHIIKVMUKHVQPARPIVBIVGQIUFHIWZSTMBTHOSLXDNDFLFYIBPMRPOHCUOLJFEMSXIJBITHPSEQUXRZEEATPHDAFGLLQAXIQAKKRVFYTPHSVFGNLEQRVMTPWAXYQSCURETQONWTINMTMUMFFHEBKQVVPWMOXXYQSMDWMESAVGTMJEUJMQGKEWMPGWKZOBLYEXUNMWTEKFHMUQMJZOBKURXMTBKQFFFTWPAJKTEAHMFLFBIUQCVXLWZEEEP")
distance_to_english_adecuated_string(strings)
