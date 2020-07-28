import os
a = 1
caisse = 0
while a == 1: #boucle infinie
    donnee()
    Popularite = 75+(Propagande+(Musee*2)+(Cinemas*2)+PopulariteArbitraireGagne)-(5*Nucleaire+PopulariteArbitrairePerdu+(population/tauxDePertePopularite)) #précalcul
    PIB = exCaisse+(Usine*2)+(Nucleaire*6)+(Ferme*4)+(Port*3)+((recettePublique/1000)*annexion)
    if Popularite <= 40 : #calcul
        caisse = PIB-(exCaisse*0.2)
    elif Popularite > 40 and Popularite <= 60:
        caisse = PIB-(exCaisse*0.1)
    elif Popularite > 60 and Popularite <= 80:
        caisse = PIB+(exCaisse*0.1)
    elif Popularite > 80 and Popularite <= 100:
        caisse = PIB+(exCaisse*0.2)
    caisse = str(caisse)
    Popularite = str(Popularite)
    print("vos caisse sont de " + caisse + " n'oubliez pas si ces caisses sont inférieurs à 10 milliard USD vos caisse sont en fait égale à 10 MDS")
    print("votre popularité est égale à:")
    print(Popularite)
    os.system("pause")
