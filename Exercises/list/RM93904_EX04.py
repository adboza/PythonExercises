# 4 – Um grande cliente seu sofreu um ataque hacker: o  servidor foi sequestrado por um software malicioso, que criptografou  todos os discos e pede a digitação de uma senha para a liberação da  máquina. E é claro que os criminosos exigem um pagamento para informar a  senha.
# Ao analisar o código do programa deles, porém, você descobre que a  senha é composta da palavra “LIBERDADE” seguida do fatorial dos minutos  que a máquina estiver marcando no momento da digitação da senha (se a  máquina estiver marcando 5 minutos, a senha será LIBERDADE120). Crie um  programa que receba do usuário os minutos atuais e exiba na tela a senha  necessária para desbloqueio. ATENÇÃO: seu programa não pode utilizar  funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente  utilizar loop.
import time

print("============================================\n           RESOLVENDO A SENHA          \n============================================\n")
minutos=int(input("Digite os minutos da hora atual no sistema: "))

# Trecho de código para resolver o fatorial
totFatorial=minutos
fatorial=0
for i in range ((minutos-1),0,-1):
    fatorial=totFatorial*i
    totFatorial=fatorial

# Trecho de código para exibir a senha
print("\nUtilize a senha:\nLIBERDADE{}".format(totFatorial))

# O texto comentado abaixo substituiria a necessidade de entrada dos minutos pelo usuário se inseridos na linha 6 deste código, substituindo o conteúdo da linha.
# minutosStr=time.strftime('%M', time.localtime())
# minutos=int(minutosStr)