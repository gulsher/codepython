is_male = False
is_tall = True
if is_male or is_tall:
    print(" you are a male and tall ")
elif is_male and not(is_tall):
    print("you are shot male")
elif not(is_male) and is_tall:
    print("you are not male but tall")
else:
    print("you are neither female or tall") 

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print(num1 , ' is greater')
    elif num2 >= num3 and num2 >= num1:
        print(num2 , ' is greater')
    else:
        print(num3 , ' is greater')

max_num(20,3,100)