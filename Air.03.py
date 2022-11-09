#Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.
#Exemples d’utilisation :
#$> python exo.py 1 2 3 4 5 4 3 2 1
#5
#$> python exo.py bonjour monsieur bonjour
#monsieur


liste = [1,2,3,4,5,4,3,2,1]
for i in liste :
    if liste.count(i) < 2:
        print(i)
