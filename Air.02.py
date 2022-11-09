def Split():
  texte_separateur = "Le choix du séparateur : "
  string_à_couper =  input("Rentrez argument : ")
  string_séparateur = input(texte_separateur)

  string_à_couper = string_à_couper.split(f"{string_séparateur}")

  for coupe in string_à_couper :
    coupe = print(coupe)

    return coupe

Split()