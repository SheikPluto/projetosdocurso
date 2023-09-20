frutas = ["Limão", "Laranja", "Abacaxi", "Morango", "Uva"]

def encontrarElemento(array):
  achei = False
  while (achei == False):
    print("Escolha a fruta:")
    print("Limão")
    print("Laranja")
    print("Abacaxi")
    print("Morango")
    print("Uva")
    elemento = input ("Escolha nessa lista qual sua fruta preferida?" )
    for i in range(len(array)):
        if (array[i] == elemento):
          achei = True
          break
    if(achei == True):
      print("Muito Bom: ", elemento)
    else:
      print("Não achei essa fruta: ", elemento, ", Tente de novo")

encontrarElemento(frutas)