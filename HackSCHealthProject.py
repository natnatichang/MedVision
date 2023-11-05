numEquip = None
EquipList = []
NumEquipList = []
combined_list1 = list(zip(EquipList, NumEquipList))
#Before doing the surgery you will first input all the equipment you know you will have for the surgery. Should not be any errors when inputting this
def PriorOR():
    print("Prior to surgery appointment checklist")
    global numEquip
    numEquip = int(input("How much medical equipment should you have?"))
    numUpdatedEquip = numEquip
    global EquipList
    global NumEquipList
    while (numUpdatedEquip != 0):
        print("You will enter one type of equipment you have and the amount of it. If you are done entering type 'Done' for 'Type of equipment prompt'. ")
        EquipType = input("Type of equipment: ")
        EquipList.append(EquipType)
        numEquip2 = int(input("Number of specific equipment: "))
        NumEquipList.append(numEquip2)
        numUpdatedEquip = numUpdatedEquip - numEquip2

    print("This is all the equipment you will have: ")
    for i in range(len(EquipList)):
        equipName = EquipList[i]
        equipNum = NumEquipList[i]
        print("\t", equipName,":",equipNum)

#when you are gathering all the tools right before the surgery
#Note for purposes of this demo you will have to enter the equipment in the same order that you did above just now in order for it to work. 
def PriorSurgery(numEquipment):
    print("\nBefore beginning surgery enter all the equipment you currently have with you")
    global numEquip
    #OriginalEquip = numEquip
    EquipAmt = 0
    numUpdatedEquip = numEquip
    PreEquipList = []
    PreNumEquipList = []
    while True:
        print("You will enter one type of equipment you have and the amount of it. If you are done entering type 'Done' for 'Type of equipment' prompt. ")
        EquipType = input("Type of equipment: ")
        if(EquipType=='Done'):
            if(EquipAmt < numEquip):
                print("YOU ARE MISSING SOMETHING. You have", numUpdatedEquip, "equipment(s) missing")
                for i in range(len(PreEquipList)):
                    if (PreEquipList[i] not in EquipList):
                        print("You are missing",PreEquipList[i])
                for i in range(len(PreNumEquipList)):
                    if (PreEquipList[i] != NumEquipList[i]):
                        print("You are missing", NumEquipList[i] - PreNumEquipList[i], EquipList[i])
            elif (EquipAmt > numEquip):
                print("YOU HAVE EXTRA EQUIPMENT. You have",EquipAmt,"equipments" )
                for i in range(len(EquipList)):
                    if (EquipList[i] not in PreEquipList):
                        print("You have extra",PreEquipList[i])
                for i in range(len(PreNumEquipList)):
                    if (PreNumEquipList[i] != NumEquipList[i]):
                        print("You have ", PreNumEquipList[i] - NumEquipList[i], "extra", EquipList[i])
            break;
        else:
            PreEquipList.append(EquipType)
            numEquip2 = int(input("Number of specific equipment: "))
            PreNumEquipList.append(numEquip2)
            EquipAmt+=numEquip2
            numUpdatedEquip = numUpdatedEquip - numEquip2

    for i in range(len(PreEquipList)):
        equipName = PreEquipList[i]
        equipNum = PreNumEquipList[i]
        print(equipName, ": ", equipNum)

    if(numUpdatedEquip>0):
        print("\nYou should have ", numEquip, " equipments")

    print("Upload a photo of surgircal equipment tray(s).")

    #print(EquipList)
    #print(NumEquipList)

def PostSurgery(numEquipment):
    print("\nPreparing to close incision. Counting all surgical equipment ")
    global numEquip
    # OriginalEquip = numEquip
    EquipAmt = 0
    numUpdatedEquip = numEquip
    PostEquipList = []
    PostNumEquipList = []
    while True:
        print("You will enter one type of equipment you have and the amount of it. If you are done entering type 'Done' for 'Type of equipment' prompt. ")
        EquipType = input("Type of equipment: ")
        if (EquipType == 'Done'):
            if (EquipAmt < numEquip):
                print("YOU ARE MISSING SOMETHING. You have", numUpdatedEquip, "equipment(s) missing")
                dangerItem1 = "scalpel"
                dangerItem2 = "needle"
                if dangerItem1 in PostEquipList:
                    print("High Caution Object was used: Scalpel was used on the body. Make sure it was not left in patient! ")
                if dangerItem2 in PostEquipList:
                    print("High Caution Object was used: Needle was used used on the body. Make sure it was not left in patient! ")
                for i in range(len(PostEquipList)):
                    if (PostEquipList[i] not in EquipList):
                        print("You are missing", PostEquipList[i])
                        continue;
                for i in range(len(PostNumEquipList)):
                    if (PostEquipList[i] != NumEquipList[i]):
                        print("You are missing", NumEquipList[i] - PostNumEquipList[i], EquipList[i])
                        continue;

            elif (EquipAmt > numEquip):
                print("Count is off. You have", EquipAmt, "equipments instead of ", numEquip)
            break;
        PostEquipList.append(EquipType)
        numEquip2 = int(input("Number of specific equipment: "))
        PostNumEquipList.append(numEquip2)
        EquipAmt += numEquip2
        numUpdatedEquip = numUpdatedEquip - numEquip2

    for i in range(len(PostEquipList)):
        equipName = PostEquipList[i]
        equipNum = PostNumEquipList[i]
        print(equipName, ": ", equipNum)

    if (numUpdatedEquip > 0):
        print("\nYou should have ", numEquip, " equipments")

    print("Upload a photo of surgircal equipment tray(s).")

def main():
    PriorOR()
    PriorSurgery(numEquip)
    PostSurgery(numEquip)

main()

