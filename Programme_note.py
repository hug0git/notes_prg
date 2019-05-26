c=0
n=0
path="C:/Users/hugod/Documents/python_simon/notes_prg/notes/"
import os
os.chdir(path)
print(os.getcwd())

#FONCTIONS
def add(files):
    name = input("Entrer le NOM de l'élève :")
    name2 = input("Entrer le PRENOM de l'élève :")
    note="0"
    while type(note) is not float and note!="Abs":
        try:
            note = input("Entrer une note (sur 20) ou Abs si l'élève était absent:")
            if note!="Abs":
                note = float(note.replace(",","."))
        except:
            print("La note n'est pas valide")
    f = open(files +".txt",'a')
    f.write(str(note) + " " + name + " " + name2)
    f.close
    
def disp(files):
    try:
        print(files)
        f=open(files + ".txt",'r')
        return(f)
    except:
        print("Désolé, ce fichier n'existe pas.")

def new(files):
    nf=open(files + ".txt",'w')
    return(nf)
    
def redir():
    import os
    os.chdir(path)

#PROGRAMME
while c!=6: #Tant que c est différent on reste dans le programme sinon si c=6 ==> "Quitter" donc on sort du programme
    print("MENU:\n 1.Nouveau devoir\n 2.Consulter des notes\n 3.Ajouter/Modifier des notes\n 4.Obtenir une moyenne\n 5.Supprimer un devoir\n 6.Quitter\n")
    try:
        c=int(input("Que souhaitez-vous faire ? (Saisissez le numéro correspondant à l'action de votre choix):"))
        if c not in [1,2,3,4,5,6]:
            print("Veuillez choisir un chiffre entre 1 et 6!")
    except:
        print("Veuillez choisir un chiffre entre 1 et 6!")
    
    #Choix 1
    if c==1:
        L=[]
        redir()
        files=input("Saisissez le nom du devoir:")
        if os.path.isfile(path + files + ".txt"):
            print("Le devoir existe déjà !")
        else:
            f=new(files)
            f.close()
            n=0
            while n not in [1,2]:
                print("Souhaitez-vous saisir des notes ?:\n 1.Oui\n 2.Non")
                try:
                    n=int(input("Que souhaitez-vous faire ? (Saisissez le numéro correspondant à l'action de votre choix):"))
                    if n not in [1,2]:
                        print("Veuillez choisir 1 ou 2!")
                except:
                    print("Veuillez choisir 1 ou 2!")
                if n==1:
                    add(files)
        
    #Choix 2
    if c==2:
        files=input("Saisissez le nom du fichier que vous souhaitez consulter:")
        folders=disp(files)
        print(folders)
        f.close()

    #Choix 3
    if c==3:
        print("test")
        
    #Choix 4
    if c==4:
        print("test")
           
    #Choix 5
    if c==5:
        print("test")
        
        
