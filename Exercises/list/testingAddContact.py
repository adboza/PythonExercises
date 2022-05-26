answer = "Y"
while answer == "Y":
    contactInfoSingle = [input("Type contact Name: "), input("Type contact phone number: ")]
    contactInfoList=[]
    contactInfoList.append(contactInfoSingle)
    answer = input("Type Y to add another contact: ").upper()



contactInfoSingle=["faldj",156165]
contactInfoList= [contactInfoSingle]
contactInfoSingle=["dfhoas",46549]
contactInfoList.append(contactInfoSingle)

contactName = input("Type the name of the contact you're looking for: ")

for contactInfoSingle in contactInfoList:
    if contactName == contactInfoSingle[0]:
        print("Name: " ,contactInfoSingle[0]," Phone number: " , contactInfoSingle[1])

# media_pares = 0.0
# for x in range(2, 51, 2):
#     print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
#     nota_aluno = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
#     media_pares = media_pares + nota_aluno
# media_p = media_pares / 25
# print("\nA MÉDIA DOS ALUNOS PARES É DE: {} PONTOS\n".format(media_p))
#
# media_impares = 0.0
# for x in range(1, 50, 2):
#     print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
#     nota_alunos = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
#     media_impares = media_impares + nota_alunos
# media_i = media_impares / 25
# print("\nA MÉDIA DOS ALUNOS ÍMPARES É DE: {} PONTOS".format(media_i))
#
# if media_p > media_i:
#     print("\nOS ALUNOS PARES TIVERAM A MAIOR MÉDIA DE NOTAS")
# else:
#     print("\nOS ALUNOS ÍMPARES TIVERAM A MAIOR MÉDIA DE NOTAS")