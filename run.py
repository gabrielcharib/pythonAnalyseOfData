#lire les fichier un par un 
# tester le format du fichier 
#gere les commencement de journer 



def lirFichier():
    global lignes
    txt = open("transact_log.txt")
    lignes =txt.readlines() 

#tester les formar du fichier 
#methode qui recupere le jour de la semaine en cours 


###########################################
# Tuesday 
# Wednesday 
# Thursday 
# Friday 
# Saturday 
# Sunday 
######################################

def recupereJourneCourant(courentDay):
    False


lirFichier()
index = 0;
totalArticles ='' #idientifier toutes les lignes 
totalclient= ''   #compter les lignes de chaque jour 
courentDay =''
day =''#variables test
newJour= False

for  ligne in lignes :
    #Test dectecter noveau jour 
    if(index > 1 and ligne[0] == 'D' ) : 
        
        #recupere je jour de la semaine 
        if(newJour == False):
            day=ligne[4:]
            print(day)
            newJour= True
        
        
    index = index +1
    newJour= False
    

 