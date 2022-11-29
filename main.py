#لحساب العدد الاكبر والاصغر بين االارقام
num1 = input("Please enter number:")
num2 = input("Please enter number:")
num3 = input("Please enter number:")
num4 = input("Please enter number:")
num5 = input("Please enter number:")

Numbers =[num1,num2,num3,num4,num5]
if num1.isdigit() and num2.isdigit() and num3.isdigit() and num4.isdigit() and  num5.isdigit():
    number1,number2,number3,number4,number5 = int(num1),int(num2),int(num3),int(num4),int(num5)

    if number1>number2 and number1>number3 and number1>number4 and number1>number5:
       print(number1)
    elif number2>number3 and number2>number4 and number2>number5 and number2>number1:
       print(number2)
    elif number3>number4 and  number3>number5 and  number3>number1 and number3>number2:
       print(number3)
    elif number4>number5 and  number4>number1 and  number4>number2 and  number4 >number3:
       print(number4)
    elif number5>number1 and number5>number2 and  number5>number3 and  number5>number4:
       print(number5)
    else:
        print("all equals")




