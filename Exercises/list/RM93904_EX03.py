# 3 – Muitos professores preferem adotar modelos  diferentes de provas quando dão aulas para turmas muito grandes. Por  essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas  são compostas por 50 alunos, solicitou que você criasse um sistema capaz  de atender ao seguinte requisito: o professor deve digitar primeiro as  notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49)  e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48,  50). O sistema deve calcular e exibir a média de cada uma das metades da  sala e informar, ao final, qual delas teve a maior nota.
# Há ainda um pedido especial do mantenedor: para que os professores  não se confundam, ao digitar cada uma das notas deve ser exibida uma  mensagem no seguinte padrão:
# VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
# POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

print("============================================\n      ESCOLA JOWELL SANT'ANA - BOLETIM     \n============================================\n")
# Início do trecho de código para receber notas de alunos ímpares
print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES\nPor favor, insira a nota do aluno com números a seguir:\n")
nota = 0
total = 0
maxImpar=-1
contador = 0
for i in range(1,51,2):
    nota=float(input("Aluno número {}:".format(i)))
    if nota < 0:
        print("O valor digitado é inválido!")
        nota=float(input("Aluno número {}: ".format(i)))
    else:
        total=nota+total
        contador+=1
        if nota>=maxImpar:
            maxImpar=nota
mediaImpar=total/contador
# Início do trecho de código para receber notas de alunos pares
print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES\nPor favor, insira a nota do aluno com números a seguir:\n")
nota = 0
total = 0
maxPar=-1
contador = 0
for i in range(2,51,2):
    nota=float(input("Aluno número {}:".format(i)))
    if nota < 0:
        print("O valor digitado é inválido!")
        nota=float(input("Aluno número {}: ".format(i)))
    else:
        total=nota+total
        contador+=1
        if nota>=maxPar:
            maxPar=nota
mediaPar=total/contador
# Início do trecho do código para exibir média de cada uma das metades da  sala e assinalar a que teve maior nota
print("\nA média da TURMA ÍMPAR foi: {:.2f} .\nA média da TURMA PAR foi: {:.2f} .".format(mediaImpar,mediaPar))
if mediaPar>mediaImpar:
    print("A maior média foi da turma Par")
elif mediaPar==mediaImpar:
    print("A média dos números pares e ímpares foi igual")
else:
    print("A média maior foi da turma ímpar")
if maxPar>=maxImpar:
    if maxPar==maxImpar:
        print("\nA maior nota foi igual para as duas turmas, nota {:.2f}!!".format(maxPar))
    else:
        print("\nA maior nota foi na TURMA PAR, nota {:.2f}!!".format(maxPar))
else:
    print("\nA maior nota foi na TURMA ÍMPAR, nota {:.2f}!!".format(maxImpar))
