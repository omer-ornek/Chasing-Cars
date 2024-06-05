car_height = int(input())
car_length = int(input())
man_height = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
l_man = ["XXXXX          " , "X   X          " , "  X            " , " X X" , "X   X"]
l_car = ["X"*car_length , "X" + " "*(car_length-2)+ "X"]
l_nons = ["XXXXX", "X   X", "  X  "]
distance = 15
diff = man_height+ 5 -car_height 
while distance >= 0:
    for j in range(diff):
        if j == 0 or j == 3 or j == 5: print(l_man[0])
        elif 0 < j < 3  : print(l_man[1])
        else: print(l_man[2])
    for i in range(diff,man_height + 5):
        if i ==0 or i == 3 or i == 5:
            if car_length < 5 and 5- distance- car_length >0 :
                if i == man_height+4 or i == diff: 
                    print(l_man[0][:distance],end="")
                    print(l_car[0],end="")
                    print(l_nons[0][(car_length + distance -5):])
                else:
                    print(l_man[0][:distance],end="")
                    print(l_car[1],end="")
                    print(l_nons[0][(car_length + distance -5):])
            else:    
                if i == man_height+4  or i == diff:  print(l_man[0][:distance],l_car[0],sep="")
                else: print(l_man[0][:distance], l_car[1],sep="")
        elif i ==1 or i == 2:
            if car_length < 5 and 5- distance- car_length >0 :
                if i == man_height+4 or i == diff: 
                    print(l_man[1][:distance],end="")
                    print(l_car[0],end="")
                    print(l_nons[1][(car_length + distance -5):])
                else:
                    print(l_man[1][:distance],end="")
                    print(l_car[1],end="")
                    print(l_nons[1][(car_length + distance -5):])
            else:
                if i == man_height+4  or i == diff:  print(l_man[1][:distance],l_car[0],sep="")
                else: print(l_man[1][:distance], l_car[1],sep="")             
        else:
            if car_length < 5 and 5- distance- car_length >0 :
                if i == man_height+4 or i == diff: 
                    print(l_man[2][:distance],end="")
                    print(l_car[0],end="")
                    print(l_nons[2][(car_length + distance -5):])
                else:
                    print(l_man[2][:distance],end="")
                    print(l_car[1],end="")
                    print(l_nons[2][(car_length + distance -5):])
            else:
                if i == man_height+4 or i == diff: print(l_man[2][:distance], l_car[0],sep="")
                else: print(l_man[2][:distance], l_car[1],sep="")
    print(l_man[2])
    print(l_man[3])
    print(l_man[4])
    print()
    distance = distance-1
distance = distance + 2
while distance <= car_length: #arabayı ters yazdır 
    for j in range(diff):
        if j == 0 or j == 3 or j == 5: print(l_man[0])
        elif 0 < j < 3  : print(l_man[1])
        else: print(l_man[2])
    for i in range(diff,man_height + 5):
        if i ==0 or i == 3 or i == 5:
            if i == diff or i == man_height+4:
                print(l_car[0][distance:car_length],end="")
                print(l_man[0][(car_length-distance):5]) #chechk if 5 or 6
            else:
                print(l_car[1][distance:car_length],end="")
                print(l_man[0][(car_length-distance):5]) #chechk if 5 or 6   
        elif i==1 or i==2:
            if i == diff or i == man_height+4:
                print(l_car[0][distance:car_length],end="")
                print(l_man[1][(car_length-distance):5]) #chechk if 5 or 6
            else: 
                print(l_car[1][distance:car_length],end="")
                print(l_man[1][(car_length-distance):5]) #chechk if 5 or 6  
        else:
            if i == diff or i == man_height+4:
                print(l_car[0][distance:car_length],end="")
                print(l_man[2][(car_length-distance):5]) #chechk if 5 or 6
            else:
                print(l_car[1][distance:car_length],end="")
                print(l_man[2][(car_length-distance):5]) #chechk if 5 or 6
    print(l_man[2])
    print(l_man[3])
    print(l_man[4])
    print()
    distance = distance + 1

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
