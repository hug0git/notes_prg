c = 0
n = 0
path = "C:/Users/hugod/Documents/python_simon/notes_prg/notes/"
import os
os.chdir(path)
print(os.getcwd())

#FONCTIONS
def add(files):
    name = input("Entrer le NOM de l'élève :")
    name2 = input("Entrer le PRENOM de l'élève :")
    note = "0"
    while type(note) is not float and note != "Abs":
        try:
            note = input("Entrer une note (sur 20) ou Abs si l'élève était absent:")
            if note != "Abs":
                note = float(note.replace(",","."))
        except:
            print("La note n'est pas valide")
    f = open(files +".txt",'a')
    f.write(str(note) + " " + name + " " + name2)
    f.close
    
def dispD(files):
    try:
        print(files)
        f=open(files + ".txt",'r')
        return(f)
    except:
        print("Désolé, ce fichier n'existe pas.")
        
def dispE(name):
    try:
        print(files)
        f=open(files + ".txt",'r')
        return(f)
    except:
        print("Désolé, ce fichier n'existe pas.")

def new(files):
    nf=open(files + ".txt",'w')
    return(nf)
   
def del(files):
    nf=open(files + ".txt",'w')
    nf.close
    return(nf)
     
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
        L = []
        redir()
        files = input("Saisissez le nom du devoir:")
        if os.path.isfile(path + files + ".txt"):
            print("Le devoir existe déjà !")
        else:
            new(files)
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
                    add(files)
        
    #2 CONSULTER
    if c == 2:
        print("Souhaitez-vous consulter les notes d'un devoir ou d'un élève ?:\n 1.Devoir\n 2.Elève\n 3.Annuler")
        try:
            co = int(input("Que souhaitez-vous faire ? (Saisissez le numéro correspondant à l'action de votre choix):"))
            if co not in [1,2,3]:
                print("Veuillez choisir 1, 2 ou 3!")
        except:
            print("Veuillez choisir 1, 2 ou 3!")
        if co == 1:
            filesD = input("Saisissez le nom du devoir que vous souhaitez consulter:")
            nd = dispD(filesD)
            print(nd)
        if co == 2:
            nameD = input("Entrer le NOM de l'élève :")
            name2D = input("Entrer le PRENOM de l'élève :")
    #AJOUTER/MODIFIER
    if c == 3:
        print("test")
        
    #MOYENNE
    if c == 4:
        print("test")
           
    #SUPPRIMER
    if c == 5:
        print("test")
        
        
