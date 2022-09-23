import numpy as np 
import string as s

# Deklarerer alfabetet, index til hver bokstav og frekvenstabellen til det engelske språket
alphabet = s.ascii_lowercase   # Alfabetet i små bokstaver 
letter_to_index = dict(zip(alphabet, range(len(alphabet))))  
index_to__letter = dict(zip(range(len(alphabet)), alphabet))

# frekvensvektoren for det engelske alfabetet 
A0 = np.array([0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 
0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 
0.060,  0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001])   

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# tar inn cipher teksten og passer på at alt er i små bokstaver, samt fjerner eventuelle mellomrom 
cipher_text = "gpoegdpvxhkggmwmzfgxxejemsyywhvpdchxcketxovmlmcwxxvzyeksezqlgsagagzmpwrlnifkowxaongykcpkqhcedctlzmxgextikdswskihweeczvmwxzlatxelsyynmwhxajsmyngplkyvlhgegltmvarmyqjmxxokghwamxxbdlltdhgyensszxwlvimrpusnbdwweodkqtdswqtdtueedssrwodavxnezikoljigexwvhedlsisnkmgmcqtmywgkrdssxvkytiwsduylcpvmgkyarmbzvyvdzjcvyfjwx".lower()
cipher_text = ''.join(i for i in cipher_text if i.isalpha())
cipher_text = [x for x in cipher_text] 
cipher_text = np.array(cipher_text)

# tar inn plain teksten og passer på at alt er i små bokstaver, samt fjerner eventuelle mellomrom 
plain_text = ''.lower()
plain_text = ''.join(i for i in plain_text if i.isalpha())
plain_text = [x for x in plain_text] 

max_keylength = 7   # maks nøkkellengde 
