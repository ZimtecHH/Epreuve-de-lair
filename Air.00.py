#Créez un programme qui
# découpe une chaîne de caractères en tableau
# (séparateurs : espaces, tabulations, retours à la ligne).

def Split():
  argument =  input("Rentrez argument : ")
  argument = argument.split(" ")
  argument = print(argument)
  return argument

Split()
