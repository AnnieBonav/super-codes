"""
All about files
Ana Bonavides AGuilar
Writing files
9/16/2020
"""
def main():
    cond = False
    while cond == False:
        print('Thank you for using my code! Here are the functions you can try:\n' + '1) Create a file\n' + '0) Exit\n')
        try:
            chooseFunc = int(input('Please enter the number of the function you want to use: '))
        except:
            print('Please enter a valid number.')
            continue

        if chooseFunc == 0:
            print('Thank you for using my program!')
            cond == True
        elif chooseFunc == 1:
            file_name = createFile()
        
        elif chooseFunc == 2:
            appendText(file_name)
        
        elif chooseFunc == 3:
            readFile()
        
        else:
            print('This function does not exist. Please enter a valid function.')



def validateFileName():
    acceptedCharacters = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w','x', 'y', 'z','1','2','3','4','5','6','7','8','9','0',' ','_']
    cond = False
    counter = 0
    while cond == False:
        file_name = str(input('Please think of the name you want you file to have' + '\n' + '1) All capital letters will be automatically lowered' + '\n' + '2)All initial and final spaces will be whiped off: ' + '\n' + '3) All spaces will be changed for lower hithens' + '\n' + 'Please write the name of your file: '))
        file_name = str.strip(file_name)
        file_name = str.lower(file_name)
        file_name = file_name.replace(' ','_')

        if file_name[0] in acceptedCharacters[0:35]:
            for i in range(len(file_name)):
                if file_name[i] in acceptedCharacters:
                    counter = counter +1
                else:
                    counter = counter

            if counter == len(file_name):
                file_name = file_name + '.txt'
                print('This is your file name: ' + file_name)
                return file_name
            else:
                print('This is not a valid name, please rememebr it can only contain letters, numbers and " ". If there are spaces they weill be automatically changed for "_" ')
        else:
            print('Remember your file name can only start with a letter.')
        


def validateText():
    #Write to file
    user_text = str(input('Please enter the text you want to add to your file: '))
    user_text = str.strip(user_text)
    user_text = str.capitalize(user_text)
    return user_text

def createFile():
    file_name = validateFileName()
    #Creates user_file.txt
    userFile = open(file_name, 'w')
    print('Your file called "' + file_name +'" has been created.')

    user_text = validateText()
    #Write into my file likes.txt
    userFile.write(user_text)
    print('Your text has been added to you file "' + file_name +'" and the file has been correctly saved & closed.')
    userFile.close()
    return file_name

def appendText(file_name):
    user_text = validateText()
    open(file_name,'a')
    file_name.write(user_text)
    file_name.close()


def readFile():
    readMe = open('likes.txt', 'r').read()
    print(readMe)




#Use of variable __name__  
if __name__=="__main__": 
    main()
