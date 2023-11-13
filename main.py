from random import randrange
import pickle

def chaine_majuscule(nom):
    for i in nom:
        if i.isupper():
            return True
    return False


# function pour enregistrer lenom
def connexion():
    nom=input("Antre non ou san espas ni let majiskil: ")
    while True:
            if " " in nom or chaine_majuscule(nom):
                nom = input('nom pa dwe gn espace oubyen let majiskil :')
                continue
                 
            return nom
# Carine men amweyyyyyyyyyyyyyyyyyyyyyyyyy Matawoos
def initialiser_database():
    try:
        with open('DB.pkl', 'rb') as file:
            database = pickle.load(file)
    except (FileNotFoundError, EOFError):
        database = {}
    return database

def jwetla(nom,database):
    reponse=" "

    if nom not in database:
        database[nom] = {'score': 0}

    while ( not reponse.lower()=="k"):
        nonb_odi=randrange(0,50)
        chans=5
        while(chans>0):

            try:
                nonb_itilizate=int(input("antre yon nonb nan enteval 0-50 ou gen "+str(chans)+" chans :"))
                if 0 <= nonb_itilizate <=50 :
                    if(nonb_itilizate < nonb_odi):
                        print(f"ou pedi paske ou chwazi {str(nonb_itilizate)} ki piti ke  nonb ki jenere a{str(nonb_odi)}")
                    elif(nonb_itilizate > nonb_odi):
                        print(f"ou pedi paske ou chwazi {str(nonb_itilizate)}  ki gro ke  nonb ki jenere a")

                    else:
                        print(f"ou genyen paske ou chwazi {str(nonb_itilizate)} ki egal ak {str(nonb_odi)} nonb ki jenere a")
                        sko = (chans-1)  * 30
                        database[nom]['score'] += sko
                        print(f"sko ou se {sko} .")
                        
                        
                        
                        break
                    chans-=1
                    
                else:
                    print("nonb ou chwazi a dwe jwenn li ant 0 a 50")
            except ValueError:
                print("antre yon nonb valid")
        sko=chans*30
    
        if(chans==0):
            print("ou pa gen chans ki rete anko .")
            print("Nonb ki te kache a se :"+str(nonb_odi))
            print("sko ou nan pati sa se :"+str(sko))
            
        print(f"nouvvo sko ou se : {database[nom]['score']}")


        reponse=input("eske ou vle rejwe? wi/non. prese nenpot touch siw vle kontinye epi k siw pap kontinye :")
        
        
        if(reponse.lower() =="k"):
            print("mesi paskew te chwazi jwe!!!!")
            break
    return database
                        

def enrejistre_database(DB):
    with open('DB.pkl', 'wb') as file:
        pickle.dump(DB, file)
    print("ou anrejistre avek sikse 'database.pkl'.")

def enrejistre_jwetla():
    database = initialiser_database()
    nom = connexion()

    if nom in database:
        ansyen_sko = database[nom]['score']
        print(f" {nom} ou rekonekte ak sikse sko avan ou an se :{ansyen_sko}.")
    else:
        ansyen_sko = 0

    database = jwetla(nom, database)
    enrejistre_database(database)

enrejistre_jwetla()





