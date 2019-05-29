c = 0
n = 0
co = 0
ce = 0
path = "C:/Users/hugod/Documents/python_simon/notes_prg/notes/"
import os
os.chdir(path)
print(os.getcwd())

#FONCTIONS
def add(file): #fonction pour ajouter une nouvelle note
    ca = 0
    while ca != 2:
        ca = 0
        name = input("Entrer le NOM de l'élève :")
        name2 = input("Entrer le PRENOM de l'élève :")
        note = "0"
        checkp = -1
        whilecheck = 0
        #permet de vérifier la validité de la note (nombre positif ou Abs)
        while whilecheck == 0: 
            try:
                note = input("Entrer une note (positive et sur 20) ou Abs si l'élève était absent:")
                if note != "Abs":
                    note = float(note.replace(",",".")) 
                    checkp = note
                    whilecheck = 1
                if checkp < 0:
                    print("La note doit être positive!")
                    whilecheck = 0
                if note == "Abs":
                    whilecheck = 1
            except:
                print("La note n'est pas valide")
                whilecheck = 0
        #ouvre le fichier et écrit nom, prénom et note
        f = open(file +".txt",'a')
        f.write(str(note) + " " + name + " " + name2 + "\n")
        f.close
        #demande si on veut saisir une autre note. Si oui on retourne au while du début sinon on quitte la boucle
        while ca not in [1,2]:
            print("Souhaitez-vous saisir une autre note ?:\n 1.Oui\n 2.Non")
            try:
                ca = int(input("Que souhaitez-vous faire ? (Saisissez le numéro correspondant à l'action de votre choix):"))
                if ca not in [1,2]:
                    print("Veuillez choisir 1 ou 2!")
            except:
                print("Veuillez choisir 1 ou 2!")
                
def edit ():
    print("lol")
    
def ask(): #fonction pour demander le nom du devoir. Si on rentre "Annuler", le programme annule l'action en cours et nous renvoie sur le menu principal
    askn = 0
    while askn == 0:
        file = input("Nom du devoir:")
        if os.path.isfile(path + file + ".txt"):
            return file
            askn = 1
        elif file == "Annuler":
            return file
        else:
            print("Désolé, ce fichier n'existe pas.")
            askn = 0
            
def getNote(file, nbligne):
    i = 0
    f=open(file + ".txt",'r')
    for i in range(1, nbligne):
        note = f.readline()
        note = note.split()
    f.close
    return note[0]
        
    
def getName(file, nbligne):
    i = 0
    f=open(file + ".txt",'r')
    for i in range(1, nbligne):
        name = f.readline()
        name = name.split()
    f.close
    return name[1]
    
def getLignFromName(file, name):
    
def lignCount(file):   
    i = 0
    f=open(file + ".txt",'r')
    for x in f:
        i += 1
    f.close
    return i
    
def dispD(file, nbc):
    f=open(file + ".txt",'r')
    for lign in range(1, nbc):
        
        print(name + " : " + note)
        
def dispE(name):
    try:
        print(files)
        f=open(files + ".txt",'r')
        return(f)
    except:
        print("Désolé, ce fichier n'existe pas.")

def new(file): #fonction pour créer un fichier
    nf=open(file + ".txt",'w')
    return(nf)
   
def delete(file): #fonction pour supprimer un fichier
    os.remove(path + file + ".txt")
     
def redir():
    import os
    os.chdir(path)

#PROGRAMME
while c != 6: #Tant que c est différent on reste dans le programme sinon si c=6 ==> "Quitter" donc on sort du programme
    print("MENU:\n 1.Nouveau devoir\n 2.Consulter des notes\n 3.Ajouter/Modifier des notes\n 4.Obtenir une moyenne\n 5.Supprimer un devoir\n 6.Quitter\n")
    try:
        c = int(input("Que souhaitez-vous faire ? (Saisissez le numéro correspondant à l'action de votre choix):"))
        if c not in [1,2,3,4,5,6]:
            print("Veuillez choisir un chiffre entre 1 et 6!")
    except:
        print("Veuillez choisir un chiffre entre 1 et 6!")
    
    #1 NOUVEAU DEVOIR
    if c == 1:
        c == 0
        L = []
        redir()
        file = input("Saisissez le nom du devoir:")
        if os.path.isfile(path + file + ".txt"):
            print("Le devoir existe déjà !")
        elif file != "Annuler":
            new(file)
            n = 0
            while n not in [1,2]:
                print("Souhaitez-vous saisir des notes ?:\n 1.Oui\n 2.Non")
                try:
                    n = int(input("Que souhaitez-vous faire ? (Saisissez le numéro correspondant à l'action de votre choix):"))
                    if n not in [1,2]:
                        print("Veuillez choisir 1 ou 2!")
                except:
                    print("Veuillez choisir 1 ou 2!")
                if n == 1:
                    add(file)
        
    #2 CONSULTER
    if c == 2:
        redir()
        c == 0
        while co!= 3:
            print("Souhaitez-vous consulter les notes d'un devoir ou d'un élève ?:\n 1.Devoir\n 2.Elève\n 3.Annuler")
            try:
                co = int(input("Que souhaitez-vous faire ? (Saisissez le numéro correspondant à l'action de votre choix):"))
                if co not in [1,2,3]:
                    print("Veuillez choisir 1, 2 ou 3!")
            except:
                print("Veuillez choisir 1, 2 ou 3!")
            if co == 1:
                print("Consulter les notes d'un devoir. Saisissez le nom du devoir ou \"Annuler\" pour sortir de ce menu")
                fileD = ask()
                if fileD != "Annuler":
                    nd = dispD(fileD)
                    print(nd)
                co = 3
            if co == 2:
                nameD = input("Entrer le NOM de l'élève :")
                name2D = input("Entrer le PRENOM de l'élève :")
                co = 3

    #3 AJOUTER/MODIFIER
    if c == 3:
        redir()
        c == 0
        while ce!= 3:
            print("Souhaitez-vous ajouter ou modifier des notes ?:\n 1.Ajouter\n 2.Modifier\n 3.Annuler")
            try:
                ce = int(input("Que souhaitez-vous faire ? (Saisissez le numéro correspondant à l'action de votre choix):"))
                if ce not in [1,2,3]:
                    print("Veuillez choisir 1, 2 ou 3!")
            except:
                print("Veuillez choisir 1, 2 ou 3!")
            if ce == 1:
                print("Ajouter une note à un devoir. Saisissez le nom du devoir ou \"Annuler\" pour sortir de ce menu")
                fileA = ask()
                if fileA != "Annuler":
                    filesA = ask()
                    add(filesA)
                ce = 3
            if ce == 2:
                print("Modifier une note d'un devoir. Saisissez le nom du devoir ou \"Annuler\" pour sortir de ce menu")
                fileU = ask()
                if fileU != "Annuler":
                    filesU = ask()
                    name = askN()
                    edit(filesU)
                ce = 3
        
    #4 MOYENNE
    if c == 4:
        print("test")
           
    #5 SUPPRIMER
    if c == 5:
        print("Supprimer un devoir. Saisissez le nom du devoir ou \"Annuler\" pour sortir de ce menu")
        fileR = ask()
        if fileR != "Annuler":
            delete(fileR)
        
        
