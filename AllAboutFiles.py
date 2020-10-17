"""
Tesla

"""


"""

Bring matrix info foma file


"""
def main ():
    cond = True
    file_name = 'friends.txt'
    separation = '-' * 50
    
    try:
        file_to_matrix(file_name)
    
    except:
        create_file(file_name)
        
    while cond == True:
        print('\n' + separation, 'Hello, these are the functions you can use:','1) Add friends to a matrix', '2) Read your file', '3) Edit your information', '4) Delete people', '6) Create another file', '0) Exit', separation, '\n', sep = '\n')
        num = validate_function_number()
        if num == 0:
            print('Thanks for using my program, bye bye.')
            cond = False

        elif num == 1:
            add_info(file_name)

        elif num == 2:
            read_file(file_name)

        elif num == 3:
            pass

        elif num == 4:
            pass
        
        elif num == 6:
            new_file = validate_file_name()
            create_file(new_file)


# This function validates that the file is written with only valid names
def validate_file_name():
    acceptedCharacters = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w','x', 'y', 'z','1','2','3','4','5','6','7','8','9','0',' ','_']
    cond = False
    while cond == False:
        counter = 0
        print('','Please think of the name you want you file to have', '1) All capital letters will be automatically lowered', '2) All initial and final spaces will be whiped off: ', '3) All spaces will be changed for lower hithens', '','Please write the name of your file: ', sep = '\n')
        file_name = str(input())
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

                # This validates the file name saving
                validate = validate_save()
                if validate == 0:
                    continue
                elif validate == 1:
                    return file_name
                else:
                    cond = True
            else:
                print('This is not a valid name, please remember it can only contain letters, numbers and " ". If there are spaces they weill be automatically changed for "_" ')
        else:
            print('Remember your file name can only start with a letter.')


            
# This function validates that the user can only enter the number of a function that exists
def validate_function_number():
    cond = True
    while cond == True:
        try:
            num = int(input('Please enter the number: '))
            if num == 0 or num ==1 or num ==2 or num == 3:
                return num
            else:
                print('I am sorry, that function does not exist, please enter a valid number.' + '\n')
                continue
        except:
            print('I am sorry, that is not a valid number.' + '\n')
            continue



# This reads the file and makes it a matrix
def file_to_matrix(file_name):
    read_file = open(file_name, 'r')
    matrix = read_file.read()
    matrix = matrix.split('\n')
    matrix.pop(0)

    for i in range(len(matrix)):
        matrix[i] = matrix[i].split(',')
    
    
    return matrix



def read_file(file_name):
    read_file = open(file_name, 'r')
    matrix = read_file.read()
    matrix = matrix.split('\n')
    matrix.pop(0)

    # I convert my files name to a string that I can use so that the user knows which informationh they are looking at
    which_file = file_name[:-4]
    which_file = which_file.capitalize()

    for i in range(len(matrix)):
        matrix[i] = matrix[i].split(',')
    
    switched_matrix = []
    for i in range(len(matrix[0])):
        row = []
        switched_matrix.append(row)
    
    # This turns the informtion in matrix in a way that it can be presente nicely to the user
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            switched_matrix[j].append(matrix[i][j])

    switched = ''
    print('\n' + 'THIS IS YOUR ' + which_file + ' INFORMATION SO FAR' + '\n')
    for i in range(len(switched_matrix)):
        row = ''
        for j in range(len(switched_matrix[i])):
            if i == 0:
                if j + 1 == len(switched_matrix[i]):
                    row = row + ':'
                else:
                    row = row + switched_matrix[i][j] + ', '
            
            else:
                if j == 0 or j == 1:
                    row = row + switched_matrix[i][j] + ' '

                elif j + 1 == len(switched_matrix[i]):
                    row = row + ';'
                else:
                    row = row + ', ' + switched_matrix[i][j]
        switched = switched + row + '\n'

    print(switched)

"""

Append to matrix

"""

# IN erethe person has the possibility of adding a frien´s information
def add_info (file_name):
    cond = True
    while cond == True:
        matrix = file_to_matrix(file_name)
        print('\n' + 'This is your friend´s matrix so far:')
        for row in matrix:
            print(row)

        # Add name
        print('\n' + 'Please enter the name of the person you want to add (without last names): ')
        name = validate_text()
        matrix[0].append(name)

        # Add last names
        print('Please enter the last names of the person you want to add: ')
        last_names = validate_text()
        matrix[1].append(last_names)

        # Gamer Tag
        print('Please enter the GamerTag of the person you are adding: ')
        gamer_tag = validate_text()
        matrix[2].append(gamer_tag)

        # Age
        print('Please enter the age of the person you are adding: ')
        age = validate_age()
        matrix[3].append(age)

        # Cellphone
        print('Please enter the cellphone of the person you are adding: ')
        cellphone = vaidate_number()
        matrix[4].append(cellphone)

        print('\n' + 'This would be your matrix:')
        for element in matrix:
            print(element)

        validate = validate_save()
        if validate == 0:
            continue
        elif validate == 1:
            save_to_file(file_name, matrix)
            cond = False
        else:
            cond = False


# I validate that the person enters 1, 0 or -1 so that the previous matrix information is saved, re-written or cancelled.
def validate_save ():
    print('\n' + 'Are you sure you aprove this information?')
    while True:
        try:
            validate = int(input('Please enter 1 if you would like to save the information, 0 if you want to write the information again or -1 to cancel: '))
            if validate == 0 or validate == 1 or validate == -1:
                return validate
            else:
                print('That is not a valid option.')
        except:
            print('That is not a valid number.')


# I take the matrix that was previously made and use it to overwrite all the previoys information
def save_to_file(file_name, matrix):
    which_file = file_name[:-4]

    title_file = 'Hey! In here you can consult all your ' + which_file + ' information.' + '\n'
    overwrite_file = open(file_name, 'w')
    overwrite_file.write(title_file)
    overwrite_file.close()

    overwrite_file = open(file_name, 'a')

    for i in range(len(matrix)):
        row = ''
        for j in range(len(matrix[i])):
            if j + 1 == len(matrix[i]):
                row = row + matrix[i][j]
            else:
                row = row + matrix[i][j] + ','
        if i + 1 != len(matrix):
            row = row + '\n'
        overwrite_file.write(row)

    overwrite_file.close()
    
"""

Validate 

"""

# This is the  function that validates the Text that you are adding to the matrix
def validate_text ():
    text = input()
    text = text.strip()
    text = text.title()

    print('This is the text you are adding: ' + text)
    return text

# This validates the age
def validate_age():
    while True:
        try:
            num = int(input('Age: '))
            if num < 0 or num > 110:
                print('I know that is not their age, please try again.')
                continue
            else:
                num = str(num)
                print('This is the age you are adding: ' + num)
                return num
        except:
            print('I am sorry, that is not a valid age, please enter a valid number.')


#This validate the number
def vaidate_number():
    while True:
        try:
            num = int(input('Number: '))
            num = str(num)
            if len(num) < 5 or len(num)> 21:
                print('I know that is not their celphone number, please try again.')
                continue
            else:
                print('This is the cellphone you are adding: ' + num)
                return num
        except:
            print('I am sorry, that is not a valid celphone, please enter a number that only contains digits.')


"""

Create an initial file


"""

# this is the first Fnction I use, which creates my base array
def create_file(file_name):
    try:
        which_file = file_name[:-4]
        cond = True
    except:
        cond = False

    while cond == True:
        title_file = 'Hey! In here you can consult all your ' + which_file + ' information.' + '\n'

        create_file = open(file_name, 'w')
        print('Your text has been added to you file "' + file_name +'" and the file has been correctly saved & closed.')
        create_file.write(title_file)
        create_file.close()

        matrix_to_file(file_name)

        cond = False
    

# After creatin my fie I add the initial matrix to it
def matrix_to_file(file_name):
    #base_matrix = [ ['Nombre', 'Annie', 'Ian'],['Apellidos', 'Bonavides Aguilar', 'Ian Doring'],['Gamertag', 'Tesla', 'Un Abduzcan'],['Age', '18', '19'],['Cellpone', '7771354737','77714518340'] ]
    base_matrix = [ ['Name'], ['Last Name'], ['Gamertag'], ['Age'], ['Cellphone']]
    matrix = base_matrix
    
    append_file = open(file_name, 'a')

    for i in range(len(matrix)):
        row = ''
        for j in range(len(matrix[i])):
            if j + 1 == len(matrix[i]):
                row = row + matrix[i][j]
            else:
                row = row + matrix[i][j] + ','
        if i + 1 != len(matrix):
            row = row + '\n'
        append_file.write(row)

    append_file.close()




#Use of variable __name__  
if __name__=="__main__": 
    main()

    
