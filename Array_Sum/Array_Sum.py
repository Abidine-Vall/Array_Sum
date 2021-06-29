#Here We define a Function that will return an array with user specified inputs 
#Note that the range in this example is [0,1000] for either the size of the array or it's elements 
#The boolean variables is handy where its the paired with the constraint 

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
#list and sum variables initialization before defining a function that will return the sum of the input array elements
l=list()
Sum=0
def simpleArraySum(l):
     for i in range(n):
         global Sum 
         Sum += l[i]
                
     return(Sum)
#main function where we instanciated an array and created a new object with the simplearraysum method and then we displayed it !
if __name__=='__main__':
 New_List=ar()
 List_Sum= simpleArraySum(New_List)
 print('The Sum is : ',List_Sum)
#Thanks and hope this helped you!
