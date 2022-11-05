#Créez un programme qui
# découpe une chaîne de caractères en tableau
# (séparateurs : espaces, tabulations, retours à la ligne).



def Split():
  texte_separateur = "Le choix du séparateur \n espace = espace \n tabulations = tab \n retour à la ligne = rl \n"

  string_à_couper =  input("Rentrez argument : ")
  string_séparateur = input(texte_separateur)

  if string_séparateur == "espace" :
    string_séparateur = " "
  if string_séparateur == "tab":
    string_séparateur = " "
  if string_séparateur == "rl":
    string_séparateur = "\n"
  else: print("erreur de séparateur")

  string_à_couper = string_à_couper.split(f"{string_séparateur}")

  for coupe in string_à_couper :
   coupe = print(coupe)

  return coupe


Split()
