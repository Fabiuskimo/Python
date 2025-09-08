nota1 = 10
nota2 = 9
nota3 = 7
nota4 = 6
idade1= 15
idade2= 16
idade3= 17
idade4 = 18
media = (nota1 + nota2 + nota3 + nota4) / 4
turma1 = "1º ano"
turma2 = "2º ano"
turma3 = "3º ano"
turma4= "Não há turma disponível para sua idade"
    
while True:    
    notaMedia = float (input("Suas notas foram 10, 9, 7 e 6. Qual foi a média de suas notas?"))

    if notaMedia == media:
        print("Você acertou a média de suas notas.")
        break
    else:
        print("A média das notas está errada.")

idade = int(input("Coloque sua idade para saber qual será sua turma: "))
if idade ==idade1:
    print ("você vai para", turma1)
elif idade ==idade2:
    print ("você vai para", turma2)
elif idade ==idade3:
    print ("você vai para", turma3)
else:
    print (turma4)

