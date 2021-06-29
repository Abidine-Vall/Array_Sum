def ar():
    My_List= list()
    input_valid= False
    while input_valid == False:
         global n
         n=int(input("The size of the array : "))
         if n in range(0,1001):
           input_valid = True 
         else:print("Value out of range!")
    input_valid= False
    for i in range(n):
        while input_valid == False:
            ele=int(input('ith element of the array!'))
            if ele in range(0,1001):
                My_List.append(ele)
                break
            else:print("Array elements invalid!")
    return(My_List)
l=list()
Sum=0
def simpleArraySum(l):
     for i in range(n):
         global Sum 
         Sum += l[i]
                
     return(Sum)
if__name__=='__main__'
 New_List=ar()
 List_Sum= simpleArraySum(New_List)
 print('The array Sum is: ',List_Sum)
