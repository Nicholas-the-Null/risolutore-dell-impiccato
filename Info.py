def Percent(lista,posizione):
    lettere=[]
    out=""
    for x in lista:
        for i,s in enumerate(x):
            if i == posizione:
                lettere.append(s)
                break
    totale=len(lettere)
    while len(lettere)!=0:
        lettera=lettere[0]
        tot_lettera=lettere.count(lettera)
        lettere=list(filter(lambda a: a != lettera, lettere))
        out+="la lettera " + lettera + " è presemte per il ben " +str(tot_lettera) + " su " + str(totale)+"\n"
    return out












