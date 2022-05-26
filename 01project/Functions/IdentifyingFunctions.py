def fillInventary(isAlist):
    answer="Y"
    while answer == "Y" :
        equipment = [input("Equipment: "), float(input("Value: ")), int(input("Serial Number: ")), input ("Department: ")]
        isAlist.append(equipment)
        answer = input("Type Y to continue: ").upper()


def showInventary(isAlist):
    for element in isAlist:
        print ("Name..........:", element[0])
        print ("Value.........:",element[1])
        print ("Serial Number.:", element[2])
        print ("Department....:", element[3])


def searchByName(isAlist):
    search=input("Type the name of the equipment you wish to search for: ")
    for element in isAlist:
        if search==element[0]:
            print("Value...:", element[1])
            print("Serial N:", element[2])


def depreciateByName (isAlist, percentage):
    depreciateValue=input("Type the name of the equipment that is going to be depreciated: ")
    for element in isAlist:
        if depreciateValue==element[0]:
            print("Former value was: ",element[1])
            element[1]*=percentage
            print("New value is: ", element[1])


def deleteBySN (isAlist):
    deleteField = (input ("Type the Serial Number you want to delete: "))
    for element in isAlist:
        if deleteField==element[2]:
            isAlist.remove(element)
    return "Item was deleted."

