def breachList(unorderedBreachList):
    #Entrada de dados das Empresas e cálculo do score que define o ranqueamento de criticidade.
    # Segue a seguinte ordem de critério:
    # 1o. Vazamento de senha, quando verdadeiro soma: 10000000000 ao score da empresa;
    # 2o. Vazamento de ajuda de senha, quando verdadeiro soma: 1000000000 ao score da empresa;
    # 3o. Vazamento de telefone, quando verdadeiro soma: 100000000 ao score da empresa;
    # 4o. Vazamento de nomes, quando verdadeiro soma: 10000000 ao score da empresa;
    # 5o. Vazamento de email, quando verdadeiro soma: 00001000000 ao score da empresa;
    # 6o. Data vazamento soma: AAAAMM(AAAA(ano) * 100 + MM(mes)) ao score da empresa.
    # Legenda da Lista = ["Nome empresa", senha(1OR0),ajuda(1OR0), telefone(1OR0), nomes(1OR0), email(1OR0)
    #                     anovazamento(AAAA),mês(MM), score(realiza cálculo)]

    #adicionando empresa Hurb
    companySingleReport = ["Hurb",1,0,1,1,1,2019,3]
    scoreBreach= (companySingleReport[1]*10000000000)+(companySingleReport[2]*1000000000)+(companySingleReport[3]*100000000)+(companySingleReport[4]*10000000)+(companySingleReport[5]*1000000)+(companySingleReport[6]*100)+(companySingleReport[7]*1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa PDL
    companySingleReport = ["PDL", 0, 0, 1, 1, 1, 2019, 10]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
                companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                              companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                              companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY3", 1, 0, 0, 0, 1, 2018, 12]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY4", 0, 1, 1, 1, 1, 2021, 3]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY5", 0, 0, 1, 1, 1, 2010, 10]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
                companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                              companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                              companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY6", 1, 0, 0, 0, 1, 2017, 12]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY7", 0, 1, 1, 0, 1, 2017, 3]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY8", 1, 0, 0, 1, 1, 2018, 12]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY9", 1, 0, 0, 0, 0, 2022, 3]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY10", 0, 0, 1, 1, 1, 2016, 10]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
                companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                              companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                              companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY11", 1, 0, 0, 0, 0, 2015, 8]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY12", 0, 0, 0, 1, 1, 2022, 3]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY13", 1, 0, 0, 0, 1, 2013, 12]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa PDL
    companySingleReport = ["COMPANY14", 0, 1, 1, 1, 1, 2017, 1]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa PDL
    companySingleReport = ["COMPANY15", 0, 0, 1, 1, 1, 2019, 11]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY16", 1, 0, 0, 0, 1, 2018, 2]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa PDL
    companySingleReport = ["COMPANY17", 0, 1, 1, 1, 1, 2012, 6]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY18", 1, 0, 0, 0, 1, 2016, 9]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa PDL
    companySingleReport = ["COMPANY19", 0, 1, 1, 1, 1, 2002, 3]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa PDL
    companySingleReport = ["COMPANY20", 0, 0, 1, 1, 1, 2020, 11]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa
    companySingleReport = ["COMPANY21", 1, 0, 0, 0, 0, 2018, 2]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)

    # adicionando empresa PDL
    companySingleReport = ["COMPANY22", 0, 1, 0, 1, 1, 2022, 5]
    scoreBreach = (companySingleReport[1] * 10000000000) + (companySingleReport[2] * 1000000000) + (
            companySingleReport[3] * 100000000) + (companySingleReport[4] * 10000000) + (
                          companySingleReport[5] * 1000000) + (companySingleReport[6] * 100) + (
                          companySingleReport[7] * 1)
    companySingleReport.append(scoreBreach)
    unorderedBreachList.append(companySingleReport)


def orderBreachList(unorderedBreachList):
    breachOrderedList=[]

    for companySingleReport in unorderedBreachList:
        breachOrderedList.append(companySingleReport[8])
    breachOrderedList.sort(reverse=True)

    numer=breachOrderedList[0]

    for companySingleReport in unorderedBreachList:
        if numer == companySingleReport[8]:
            print("\nO pior vazamento foi da empresa: {}".format(companySingleReport[0]))

    print("\nRanking dos vazamentos por criticidade:", "\nPOSIÇÃO) NOME DA EMPRESA, MÊS/ ANO")

    for i in range(0,len(breachOrderedList)):
        for companySingleReport in unorderedBreachList:
            score=breachOrderedList[i]
            if score == companySingleReport[8]:
                ordem=i+1
                print(ordem,") ",companySingleReport[0],", ",companySingleReport[7],"/",companySingleReport[6])

