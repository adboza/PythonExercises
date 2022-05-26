# 1 – Você foi procurado por um aluno do curso de Produção  Multimídia do FIAP ON para desenvolver um trabalho em parceria: um  serviço em que as pessoas possam usar um estúdio profissional para  gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha  dinheiro por meio de um sistema de assinaturas e de um bônus calculado  por uma porcentagem sobre o faturamento que o canal do cliente obteve ao  longo do ano.
# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do  cliente, o faturamento anual dele e que calcule e exiba qual o valor do  bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a  porcentagem de acordo com cada nível de assinatura:
# nivel || porcentagem sobre o faturamento
# basic || 30%
# Silver || 20%
# Gold || 10 %
# Platinum || 5%

faturamentoAnual=0
faturamentoAnual=float(input("Insira o faturamento anual do canal:\nAtenção utilize \".\" \"PONTO\" para informar valor decimal.\n R$ "))
if faturamentoAnual<0:
    print("O valor digitado é inválido!")
    faturamentoAnual = float(input("Insira o faturamento anual do canal:\nAtenção utilize \".\" \"PONTO\" para informar valor decimal.\n R$ "))
tipoAssinatura=int(input("Insira número correspondente ao tipo de assinatura contratado:\n1 - Basic\n2 - Silver\n3 - Gold\n4-Platinum\n"))
if (tipoAssinatura<1 or tipoAssinatura>4):
    print("Opção inválida!")
    tipoAssinatura = int(input("Insira número correspondente ao tipo de assinatura contratado:\n1 - Basic\n2 - Silver\n3 - Gold\n4-Platinum\n"))
if tipoAssinatura == 4:
    nomeAssinatura="Platinum e paga bonus de 5% sobre o faturamento"
    bonusAssinatura=0.05
elif tipoAssinatura == 2:
    nomeAssinatura = "Silver e paga bonus de 20% sobre o faturamento"
    bonusAssinatura = 0.2
elif tipoAssinatura == 3:
    nomeAssinatura = "Gold e paga bonus de 10% sobre o faturamento"
    bonusAssinatura = 0.1
else:
    nomeAssinatura = "Basic e paga bônus de 30% sobre o faturamento"
    bonusAssinatura = 0.3
print("Sua assinatura é {}.\nO faturamento informado foi de R$ {:.2f}.\n\nO bonus total que deve ser pago é R$ {:.2f}.\nObrigado!" .format(nomeAssinatura,faturamentoAnual,(bonusAssinatura*faturamentoAnual)))