#Créez un programme qui
# découpe une chaîne de caractères en tableau
# (séparateurs : espaces, tabulations, retours à la ligne).

def Split(string_séparateur):
  string_à_couper =  input("Rentrez argument : ")
  string_à_couper = string_à_couper.split(f"{string_séparateur}")
  for coupe in string_à_couper :
   coupe = print(coupe)
  return coupe


Split(" ")
