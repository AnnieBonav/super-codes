"""
All about files
Ana Bonavides AGuilar
Writing files
9/16/2020
"""
def main():
    print('Thank you for using my code! Here are the functions you can try:\n' + '1) Create a file.\n' + '2) Append to file.\n' + '3) Read your file.\n' + '0) Exit' + '\n')

    try:
        fileNamesToArray()
    except:
        # I create the file 'files_names.txt' with the variable files_var. 
        files_var = open('files_names.txt','w')
        files_var.close()

    while True:
        try:
            chooseFunc = int(input('\nPlease enter the number of the function you want to use, or 9 if you want to read the Menu again: '))
        except:
            print('Please enter a valid number.')
            continue

        if chooseFunc == 0:
            print('Thank you for using my program!')
            break

        elif chooseFunc == 9:
            print('Thank you for using my code! Here are the functions you can try:\n' + '1) Create a file.\n' + '2) Append to file.\n' + '3) Read your file.\n' + '0) Exit' + '\n')

        elif chooseFunc == 1:
            createFile()
        
        elif chooseFunc == 2:
            appendText()
        
        elif chooseFunc == 3:
            readFile()
        
        else:
            print('This function does not exist. Please enter a valid function.')


def createFile():
    file_name = validateFileName()
    appendToFileNames(file_name)

    # I bring the file names array to the function
    names_array = fileNamesToArray()
    print('These are all your files: ',names_array)

    #Creates create_file variable which will create the user´s file with the filename they chose
    create_file = open(file_name, 'w')
    print('Your file called "' + file_name +'" has been created.')

    user_text = validateText()
    #Write into my file likes.txt
    create_file.write(user_text)
    print('Your text has been added to you file "' + file_name +'" and the file has been correctly saved & closed.')
    create_file.close()



def appendText():
    names_array = fileNamesToArray()

    print('These are the files you have created, please choose the one you wnat to change: ' + '\n',names_array,'\nRemember that the first name you see is #0\n')
    file_chosen = int(input('Please enter the number of the file you want to change: '))

    file_name = names_array[file_chosen]
    print('This will be the file you are changing: ' + file_name)

    user_text = validateText()
    append_file = open(file_name,'a')
    append_file.write(user_text)
    append_file.close()



def readFile():
    names_array = fileNamesToArray()

    print('These are your files:\n',names_array)
    file_chosen = int(input('Please enter the number of the file you want to read: '))
    file_name = names_array[file_chosen]
    read_file = open(file_name, 'r').read()
    print(read_file)

"""
Main File with all file names (files_names.txt) functions

"""

# This function appends the new created file name to the files_names text file
def appendToFileNames(file_name):
    files_var = open('files_names.txt','a')
    files_var.write(file_name)
    files_var.write(',')

    files_var.close()


# This is the function I use to convert my file that has the names to an array used to modify the other files.
def fileNamesToArray():
    files_var = open('files_names.txt','r')
    content = files_var.read()
    names_array = content.split(',')

    return names_array


def validateFileName():
    acceptedCharacters = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w','x', 'y', 'z','1','2','3','4','5','6','7','8','9','0',' ','_']
    cond = False
    counter = 0
    while cond == False:
        file_name = str(input('\nPlease think of the name you want you file to have' + '\n' + '1) All capital letters will be automatically lowered' + '\n' + '2) All initial and final spaces will be whiped off: ' + '\n' + '3) All spaces will be changed for lower hithens' + '\n\n' + 'Please write the name of your file: '))
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
    user_text = user_text + '\n'
    return user_text


#Use of variable __name__  
if __name__=="__main__": 
    main()
