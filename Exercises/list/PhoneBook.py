def addContact(contactInfoList):
    answer = "Y"
    while answer == "Y":
        contactInfoSingle = [input("Type contact Name: "), input("Type contact phone number: ")]
        contactInfoList.append(contactInfoSingle)
        answer = input("Type Y to add another contact: ").upper()
    for name in contactInfoList:
        print(name)


def searchContact(contactInfoList):
    contactName = input("Type the name of the contact you're looking for: ")
    for contactInfoSingle in contactInfoList:
       if contactName == contactInfoSingle[0]:
             print("Name: " ,contactInfoSingle[0],"\n" , "Phone number: " , contactInfoSingle[1])

def numbersList (numberList):
    numberList = [1, 7, 7, 5, 2, 9, 9, 9, 2]
    print("The list is: {}".format(numberList))
    print("In this list the number 9 appears {} times".format(numberList.count(9)))
    print("In this list the number 2 appears {} times".format(numberList.count(2)))
    numberList.reverse()
    print("See the list reversed: {}" .format(numberList))
    numberList.sort()
    print("This is the ordered list: {}" .format(numberList))
    print("the list has {} items." .format(len(numberList)))
    print("The sum of the list items is {}." .format(sum(numberList)))
