# 2 – Os alunos da sua turma fizeram uma votação para  escolher qual dia da semana é o melhor para a realização das lives.  Desenvolva um programa em que o usuário informe a quantidade de votos  que cada um dos 5 dias da semana (segunda-feira, terça-feira,  quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba  qual dia foi o escolhido.


print("============================================\nCONTAGEM DE VOTOS PARA REALIZAÇÃO DA LIVE!!!\n============================================\n")
# Início do código para que o usuário informe a quantidade de votos  que cada um dos 5 dias da semana
votosSegunda = int(input("Insira o número de votos para cada dia da semana que aparecerá na sequência:\nSegunda feira: "))
if votosSegunda<0:
    print("O valor digitado é inválido!")
    votosSegunda = float(input("Insira valor válido para:\nSegunda Feira: "))
votosTerca = int(input("Terça feira: "))
if votosTerca<0:
    print("O valor digitado é inválido!")
    votosTerca = float(input("Insira valor válido para:\nTerça Feira: "))
votosQuarta= int(input("Quarta feira: "))
if votosQuarta<0:
    print("O valor digitado é inválido!")
    votosQuarta = float(input("Insira valor válido para:\nQuarta Feira: "))
votosQuinta= int(input("Quinta feira: "))
if votosQuinta<0:
    print("O valor digitado é inválido!")
    votosQuinta = float(input("Insira valor válido para:\nQuinta Feira: "))
votosSexta= int(input("Sexta feira: "))
if votosSexta<0:
    print("O valor digitado é inválido!")
    votosSexta = float(input("Insira valor válido para:\nSexta Feira: "))

# Início do trecho de código para verificar e exibir mais votado
print("\n\n============================================\n            OLHA O RESULTADO!!!             \n============================================\n")
for i in range (0,5):
    if i==0:
        if votosSegunda>=votosTerca and votosSegunda>=votosQuarta and votosSegunda>=votosQuinta and votosSegunda>=votosSexta:
            print("Segunda feira foi mais votada com {} votos!".format(votosSegunda))
            if votosSegunda==votosTerca or votosSegunda==votosQuarta or votosSegunda==votosQuinta or votosSegunda==votosSexta:
                print("Houve empate!!")
    elif i==1:
        if votosTerca>=votosSegunda and votosTerca>=votosQuarta and votosTerca>=votosQuinta and votosTerca>=votosSexta:
            print("Terça feira foi mais votada com {} votos!".format(votosTerca))
            if votosTerca==votosSegunda or votosTerca==votosQuarta or votosTerca==votosQuinta or votosTerca==votosSexta:
                print("Houve empate!!")
    elif i==2:
        if votosQuarta>=votosSegunda and votosQuarta>=votosTerca and votosQuarta>=votosQuinta and votosQuarta>=votosSexta:
            print("Quarta feira foi mais votada com {} votos!".format(votosQuarta))
            if votosQuarta==votosSegunda or votosQuarta==votosTerca or votosQuarta==votosQuinta or votosQuarta==votosSexta:
                print("Houve empate!!")
    elif i==3:
        if votosQuinta>=votosSegunda and votosQuinta>=votosQuarta and votosQuinta>=votosTerca and votosQuinta>=votosSexta:
            print("Quinta feira foi mais votada com {} votos!".format(votosQuinta))
            if votosQuinta==votosSegunda or votosQuinta==votosQuarta or votosQuinta==votosTerca or votosQuinta==votosSexta:
                print("Houve empate!!")
    elif i==4:
        if votosSexta>=votosSegunda and votosSexta>=votosQuarta and votosSexta>=votosQuinta and votosSexta>=votosTerca:
            print("Sexta feira foi mais votada com {} votos!".format(votosSexta))
            if votosSexta==votosSegunda or votosSexta==votosQuarta or votosSexta==votosQuinta or votosSexta==votosTerca:
                print("Houve empate!!")

