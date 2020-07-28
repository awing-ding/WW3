import os
a = 1
caisse = 0
def donnee():
  exCaisse = int(input("quels sont vos anciennes caisses ? "))
  recettePublique = int(input("quels sont vos recette publique en % mais sans le <<%>> ?"))
  annexion = int(input("quel est le total du PIB des pays que vous avez annexé ?"))
  tauxDePertePopularite = int(input("par combien votre population est-elle divisé pour calculer votre popularité (si vous ne savez pas, contactez le staff) ?"))
  population = int(input("quel est votre population ?"))
  Musee = int(input("combien de musée avez vous construit ?"))
  Propagande = int(input("combien de propagande avez vous fait ?"))
  Cinemas = int(input("combien de cinéma avez vous construit ?"))
  Usine = int(input("combien d'usine avez vous construit ?"))
  Nucleaire = int(input("combien de centrale nucléaire avez vous construit ?"))
  Ferme = int(input("combien de ferme avez vous construit ?"))
  Port = int(input("combien de port avez vous construit ?"))
  PopulariteArbitrairePerdu = int(input("Combien de popularité les MJ/roll vous ont fait perdre ?"))
  PopulariteArbitraireGagne = int(input("Combien de popularité les MJ/roll vous ont fait gagner ?"))
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
