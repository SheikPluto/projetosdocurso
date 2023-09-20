#Desenvolva um programa que recebe do usuário nome completo
# e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário 
# e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


def idadeAtual():
  id = False  
   
  while (id == False):
    try:
        nomeCompleto = str(input(' Qual o seu Nome Completo? '))
        dataNasc = float(input(' Qual o ano de Nascimento? '))
        anoAtual = 2022
        idadeTotal = anoAtual - dataNasc
        
        if dataNasc > 2022 < 1921:
          print("Digite um ano entre 1922 e 2021")          
        else:
          print("Ótimo ,", nomeCompleto, "sua idade é: ", int(idadeTotal), "anos")
          id == True
          break

    except:
      print("digite um numero válido")


idadeAtual()