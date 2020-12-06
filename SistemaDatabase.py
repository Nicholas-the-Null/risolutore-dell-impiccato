import os
def duplicati(list):
    """elimina duplicati in un database"""
    if os.path.exists(file) is False:
        return "file non trovato"
    else:
        x=open(file,"r")
        parole=x.readlines()
        x.close()
        return list(dict.fromkeys(parole))


def Unica_Lunghezza(file,lunghezza):
    nuove_parole=[]
    if os.path.exists(file) is False:
        return "file non trovato"
    else:
        x=open(file,"r")
        parole=x.readlines()
        x.close()
        for x in parole:
            if lunghezza==len(x.strip("\n")):
                nuove_parole.append(x)
        return nuove_parole




def Elimina_Lunghezza(file,lunghezza):
    nuove_parole=[]
    if os.path.exists(file) is False:
        return "file non trovato"
    else:
        x=open(file,"r")
        parole=x.readlines()
        x.close()
        for x in parole:
            if lunghezza!=len(x.strip("\n")):
                nuove_parole.append(x)
        return nuove_parole



def Elimina_Iniziale(iniziale,file):
    nuove_parole=[]
    if os.path.exists(file) is False:
        return "file non trovato"
    else:
        x=open(file,"r")
        parole=x.readlines()
        x.close()
        for x in parole:
            if iniaziale!=x[0]:
                nuove_parole.append(x)
        return nuove_parole

def Ordina(file):
    if os.path.exists(file) is False:
        return "file non trovato"
    else:
        x=open(file,"r")
        parole=x.readlines()
        x.close()
        return parole.sort()

def Cat(file1,file2):
    nuove_parole=[]
    if os.path.exists(file1) is False or os.path.exists(file2) is False:
        return "file non trovato"
    else:
        x=open(file1,"r")
        database_1=x.readlines()
        x.close()
        x=open(file2,"r")
        database_2=x.readlines()
        x.close()
        nuove_parole=database_1+database_2
        nuove_parole=list(dict.fromkeys(nuove_parole))
        return nuove_parole


def Uncat(file1,file2):
    nuove_parole=[]
    if os.path.exists(file1) is False or os.path.exists(file2) is False:
        return "file non trovato"
    else:
        x=open(file1,"r")
        database_1=x.readlines()
        x.close()
        x=open(file2,"r")
        database_2=x.readlines()
        x.close()
        database_1=list(dict.fromkeys(database_1))
        database_2=list(dict.fromkeys(database_2))
        for x in database_2:
            if x in database_1:
                database_1.remove(x)
                
                
        return database_1


def LowerAll(file):
    nuove_parole=[]
    if os.path.exists(file) is False:
        return "file non trovato"
    else:
        x=open(file1,"r")
        database=x.readlines()
        x.close()
        for x in database:
            nuove_parole.append(x.lower())
        return nuove_parole
    

def Scrivi(file,lista):
    x=open(file,"w+")
    x.write("")
    x.close()
    x=open(file,"a")
    for i in lista:
        x.write(i)
    x.close()



###########################################################################
#                                                                        ##
#                                                                        ##
#                                                                        ##
#           Sistema velocemente i database                               ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
#                                                                        ##
###########################################################################
    
