""""
INTEGRANTES
Annie Bonavides ft Ar-P
Menu
"""

#Defining main
def main():
    condition = False
    while condition == False:
        try:
            print('\n' + 'Welcome to our program, here are the functions you can use:','\n','1) Get maximum divisor','\n','2) Painting Pyramids','\n','0) Exit','\n')
            num1 = int(input('Please enter the number of the function you want to use: '))

            if num1 == 0:
                #We give the user the choice to exit the program
                print('Thank you for using our program. Please return soon.')
                condition = True
            elif num1 == 1:
                #We call the function maximum divisor
                mcd()
            elif num1 == 2:
                #We call the function paint_drawing which creates the pyramid
                paint_drawing()
                
            else:
                print('Please enter a valid number.')
                continue
            
            condition = True
        except:
            print('This is not a valid number.' + '\n')

#We define pide_numeros function which validates the two whole numbers that will be used in the maximum common divisor function
def pide_numeros():
    nums = False
    while nums == False:
        try:
            num1 = int(input('Please enter your first number: '))
            num2 = int(input('Please enter your second number: '))
            nums = True
        except:
            print('These were not valid numbers.','\n')

    print('These are the numbers you chose: ',num1,num2,'\n')
    return num1, num2

#We define the function that gets the maximum common divisor of two given numbers (previously validated in pide_numeros)
def mcd():
    num1, num2 = pide_numeros()

    divisores = []
    mcd = 1
    if num1 > num2:
        num_menor = num2
    else:
        num_menor = num1
    
    for i in range(2, num_menor+1):
        while (num1%i == 0 and num2%i == 0):
            divisores.append(i)
            num1=num1/i
            num2=num2/i
    
    for i in range(len(divisores)):
        mcd = mcd * int(divisores[i])
    
    print('Your maximum divisor is: ',mcd,'\n')
    continue_validate()
    
#We define the function data_drawing so that the character used i paint_drawing (our pyramid) is validated
def data_drawing():
    charUse = False
    while charUse == False:
        sym = input('Please enter your symbol: ' + '\n' + 'Here are the symbols you can use: *, =, +' + '\n')
        if sym == '*' or sym == '+' or sym == '=':
            charUse = True
        else:
            print('This is not a valid symbol.','\n')
            continue
    return sym

#We define the function num_drawing so that the user can choose the ammount of lines that their drawing is going to have
def num_drawing():
    validate = False
    while validate == False:
        try:
            num = int(input('Please enter how many lines you want your drawing to have: '))
            validate = True
        except:
            print('This is not a valid number.' + '\n')
            continue
    return num

        
#We define the function paint_drawing which uses the character validated in pide_character to print the pyramids (whith one of the 3 characters available)
def paint_drawing():
    #We establish the variable "blank space (bla)" in case we want to change the blank space for another character, in the future
    bla = ' '
    #We establish the variable sym (symbol) and give it the value that our function "data_drawing" returns (which validates the symbol)
    sym = data_drawing()

    #We establish a variable num (number) and give it the value that our function "num_Drawing" returns (Which validates the number)
    num = num_drawing()

    #We print a double space so the pyramids are framed
    print('\n' + '\n')

    #We define the way our for is going to print the pyramids
    for i in range (1, num+1):
        print(sym*(num-(i-1))  + bla*i + sym*i  +  bla*(num-(i-1))  +  bla*(num-(i-1))  + sym*i + bla*i + sym*(num-(i-1)))
    
    #We print a double space so the pyramids are framed
    print('\n' + '\n')
    continue_validate()

#We define the function continue_validate 
def continue_validate():
    validate = False
    while validate == False:
        enter_continue = input('Please click enter if you want to continue, or write 0 if you want to exit.' + '\n')
        if enter_continue == '':
            main()
        elif enter_continue == '0':
            print('Thank you for using our program. See you soon :)' + '\n')
            validate = True
        else:
            print('That is not a valid input.' + '\n')
            continue


#Use of variable __name__  
if __name__=="__main__": 
    main()

