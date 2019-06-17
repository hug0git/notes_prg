
def lignCount(file):   # fonction qui sert a compter le nombre de ligne
    i = 0
    f=open(file + ".txt",'r')
    for x in f:
        i += 1   #i = i + 1
    f.close
    return i
    
nbligne = lignCount(fichier)

