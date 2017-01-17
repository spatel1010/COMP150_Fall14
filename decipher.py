# decipher.py
# Shivam Patel

def createDict():
    dec = dict()
    dec[z] = 't'
    dec[r] = 'c'
    dec[e] = 's'
    dec[c] = 'i'
    dec[y] = 'a'
    dec[q] = 'b'
    dec[o] = 'l'
    dec[m] = ' '
    dec[w] = 'p'
    dec[t] = 'm'
    dec[b] = 'h'
    dec[s] = 'u'
    dec[p] = 'e'
    dec[y] = 'a'
    return dec

def decode(decoder,phrase):
    unMix = ''
    phrase = 'zbcemtsezmqpmzbpmwoyrp'
    for x in phrase:
        unMix = unMix + decoder[x]
    return unMix
        

def main():
    diction = createDict()
    coded =  'zbcemtsezmqpmzbpmwoyrp'
    decoded = decode(diction,coded)
    decode = decode()
    print("Coded", coded, "Decoded", decoded.format(**diction))
    
main()

