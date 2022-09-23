import numpy as np
import config as cng 

# Finn nøkkellengden 
def FindKeyLength(cipher_text, max_keylength): 
    orignial_cipher_text = cipher_text
    coincidences = 0    # antall ganger det er like bokstaver på samme plass 
    tmp = cipher_text
    keylength = 0

    # flytt en gang mot høyre for hver runde og finn antall koinsidenser for orginalteksten P0 og Pi 
    for i in range(max_keylength): 
        tmp = np.insert(tmp, 0, 0)          # setter inn en ny null i begynnelsen av arrayet
        tmp = tmp[0:len(cipher_text)]    # tilpasser lengden på arrayet 
        new_coincidences = np.sum(tmp == orignial_cipher_text)  # sammenlikner den nye teksten med den orgonale 

        if new_coincidences > coincidences: 
            coincidences = new_coincidences 
            keylength = i + 1   # i + 1 fordi vi begynner å telle på 0   

    return keylength    # returnerer nøkkellengden 
        

def FindKey(cipher_text, keylength): 
    # del inn i blokker så lenge i ikke er større enn nøkkellengden 
    key = []              # Her lagres bokstavene til nøkkelen etterhvert som koden finner de
    array = []            # Lager et array som skal holde flere mindre arrays med posisjon som svarer til nøkkellengden 

    # lager en loop som kjører gjennom hele nøkkellengden 
    for i in range(key_length): 
        sub_arr = []      # For å lagre alle verdiene i de mindre arrayene 
        frequency = []     # lager er tmp list for å oppbevare frekvensen av bokstaver i de ulike sub arrayene 

        pos = i
        cross_product = 0     # Kryssproduktet 


        # Lager subarrays, antallet subarrays bestemmes av nøkkellengden 
        for j in range((len(cipher_text))//key_length): 
            tmp = cipher_text[pos]
            sub_arr.append(tmp)
            pos += key_length   # oppdaterer posisjonen med lengden på nøkkelen 

        # Finner hvor mange ganger hver bokstaver er oppdaget i sub_arrayet 
        # og deler på lengden av sub_arrayet for å finne frekvensen 
        for k in range(len(cng.alphabet)): 
            occurrence = (sub_arr.count(cng.alphabet[k]))
            frequency.append((occurrence/len(sub_arr)))

        # shift og sammelikn med A0
        for l in range(len(cng.alphabet)): 
            new_frequency = np.roll(frequency, -l)                     # shifter l ganger 

            # regner ut kryssproduktet og sjekker om det nye kryssproduktet er høyere enn det forje 
            new_cross_product = np.multiply(cng.A0, new_frequency)   
            new_cross_product = sum(new_cross_product)

            if cross_product < new_cross_product: 
                cross_product = new_cross_product
                shift = l

        # gjør om antall shift til en bokstav og legg til i key 
        shift += ord('a')
        key.append(chr(shift))
    key = "".join(key)
    return key


def Decryption(cipher_text, key):
    plain_text = []
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i%5])+26)%26
        x += ord('a')
        plain_text.append(chr(x))
    plain_text = "".join(plain_text)
    return plain_text
    



if __name__ == "__main__": 
    key_length = FindKeyLength(cng.cipher_text, cng.max_keylength)      # Finne lengden på nøkkelen 
    key = FindKey(cng.cipher_text, key_length)                          # Finner nøkkelen  
    plain_text = Decryption(cng.cipher_text, key)                       # Dekrypterer teksten 
    print("Original/Decrypted Text :",plain_text)
