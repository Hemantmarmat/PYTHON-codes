print("1 - addition")
print('2 - subtraction')
print("3 - divide")
print("4 - multiplication")

option = int(input("chosse an opreatin"))

if(option in [1,2,3,4]):
    num1=int(input("enter any number"))
    num2=int(input("enter any number"))

    if(option==1):
        result = num1+num2
    elif(option==2):
        result = num1-num2
    elif(option==3):
        result = num1/num2
    elif(option==4):
        result = num1*num2

else: 
    print("Invailid opreation enterd")

print("the result of the opreation is {}".format (result))