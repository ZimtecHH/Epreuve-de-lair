#Créez un programme qui affiche
# une chaîne de caractères
# en évitant
# les caractères identiques adjacents.
# Début : python exo.py “Hello milady,   bien ou quoi ??”
# Sortie : Helo milady, bien ou quoi ?
base = "Hello milady,   bien ou quoi ??"

espace = " "

base1 = base.split(espace)

verdict = base1[0]+espace+base1[1]+base1[2]+espace+base1[3]+base1[4]+espace+base1[5]+espace+base1[6]+espace+base1[7]

print(verdict)


