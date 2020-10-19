"""
Tesla

"""


def main ():
    cond = True
    base_file_name = 'friends.txt'

    separation = '-' * 50
    
    try:
        file_to_matrix(base_file_name)
    
    except:
        files_var = open('files_names.txt','w')
        files_var.close()
        create_file(base_file_name)
        
    while cond == True:
        print('\n' + separation, 'Hello, these are the functions you can use:','1) Add friends to a matrix', '2) Read your file', '3) Edit your information', '4) Delete people', '6) Create another file', '0) Exit', '\n', sep = '\n')
        num = validate_function_number()
        if num == 0:
            print('Thanks for using my program, bye bye.')
            cond = False

        elif num == 1:
            add_info()

        elif num == 2:
            file_name = file_names_to_array()
            read_file(file_name)

        elif num == 3:
            edit_info()

        elif num == 4:
            delete_info()
        
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
    separation = '-' * 50

    functions = [0,1,2,3,4,5,6]
    cond = True
    while cond == True:
        try:
            num = int(input('Please enter the number: '))
            print(separation + '\n')
            if num in functions:
                return num
            else:
                print('I am sorry, that function does not exist, please enter a valid number.' + '\n')
                continue
        except:
            print('I am sorry, that is not a valid number.' + '\n')
            continue




"""


Bring matrix info to file


"""


# This reads the file and makes it a matrix
def file_to_matrix(file_name):
    read_file = open(file_name, 'r')
    matrix = read_file.read()
    matrix = matrix.split('\n')
    matrix.pop(0)

    for i in range(len(matrix)):
        matrix[i] = matrix[i].split(',')
    
    
    return matrix



"""

RUD Matrix


"""


def read_file(file_name):

    separation = '-' * 50
    read_file = open(file_name, 'r')
    matrix = read_file.read()
    matrix = matrix.split('\n')
    matrix.pop(0)

    # I convert my files name to a string that I can use so that the user knows which informationh they are looking at
    which_file = file_name[:-4]
    which_file = which_file.upper()

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
    
    for i in range(len(switched_matrix)):
        row = ''
        for j in range(len(switched_matrix[i])):
            if i == 0:
                if j == 0:
                    row = 'Complete name, '

                elif j == 1:
                    pass

                elif j + 1 == len(switched_matrix[i]):
                    row = row + switched_matrix[i][j] + ':'

                else:
                    row = row + switched_matrix[i][j] + ', '
            
            else:
                if j == 0:
                    row = '[' + str(i) + '] ' + switched_matrix[i][j] + ' '

                elif j + 1 == len(switched_matrix[i]):
                    row = row + switched_matrix[i][j] + ';'
                    
                else:
                    row = row + switched_matrix[i][j] + ', ' 

        switched = switched + row + '\n'

    print(separation, 'THIS IS YOUR ' + which_file + ' INFORMATION SO FAR' + '\n', switched, separation, sep = '\n', end = '\n\n')


def choose_file():
    pass

# Edit matrix informaion
def edit_info():
    file_name = file_names_to_array()
    cond = True
    while cond == True:
        read_file(file_name)
        matrix = file_to_matrix(file_name)

        # This decides which matrix person they will delete
        num_column = validate_matrix_row(matrix)

        #This shows the info of the person you chose
        for i in range(len(matrix)):
            #row = ''
            for j in range(len(matrix[i])):
                if j == num_column:
                    print( '[', i+1, '] ', matrix[i][j], sep = '')
                   
        num_row = validate_column_number()
        num_row = num_row -1

        print('This is the data you will edit:', matrix[num_row][num_column])
        print('NEW DATA')

        if num_row == 0 or num_row == 1 or num_row == 2:
            value = validate_text()
        elif num_row == 3:
            value = validate_age()
        elif num_row == 4:
            value = validate_number()
             
        # I change the value
        matrix[num_row][num_column] = value
        
        print('\n' + 'THIS WOULD BE YOUR INFORMATION')
        #This shows the new info
        for i in range(len(matrix)):
            #row = ''
            for j in range(len(matrix[i])):
                if j == num_column:
                    print( '[', i+1, '] ', matrix[i][j], sep = '')

        validate = validate_save()
        if validate == 0:
            continue
        elif validate == 1:
            save_to_file(file_name, matrix)
            cond = False
        else:
            cond = False

        


def validate_column_number():
    while True:
        try:
            num = int(input('Please enter the number of data you want to edit: '))
            if num < 1 or num > 5:
                print('Please enter a valid data number')
            else:
                return num
        except:
            print('Please enter a valid number.')


def delete_info():
    file_name = file_names_to_array()
    cond = True
    while cond == True:
        read_file(file_name)
        matrix = file_to_matrix(file_name)

        # This decides which matrix person they will delete
        num = validate_matrix_row(matrix)
        print('This is the number you chose: ', num)

        #This removes the index
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == num:
                    matrix[i].pop(j)

        print('\n' + 'This would be your information:')
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
            


# This function is so that users enter the numnber of the person´s index they want to edit/delete
def validate_matrix_row(matrix):

    while True:
        try:
            num = int(input('Please enter the number of the person you want to edit/remove: '))
            if num == 0:
                print('Please enter a valid number, this person doesn´t exist.' + '\n')
                continue
            else:
                try:
                    trying = matrix[0][num]
                    return num
                except:
                    print('Please enter a number of a person that exists.' + '\n')
                    continue
        except:
            print('Please enter a valid number.' + '\n')
            continue



# IN erethe person has the possibility of adding a frien´s information
def add_info ():
    file_name = file_names_to_array()

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
        cellphone = validate_number()
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

    text = input('Please enter your text: ')
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
def validate_number():
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
        
        # Append to file name
        append_file_name = open('files_names.txt', 'a')
        append_file_name.write(file_name)
        append_file_name.write('\n')
        append_file_name.close()

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



def file_names_to_array():
    files_var = open('files_names.txt','r')
    content = files_var.read()
    names_array = content.split('\n')

    names_array.pop(-1)

    names_string = ''
    #print(names_array)
    for i in range(len(names_array)):
        names_string = names_string + '[' + str(i + 1) + '] ' + names_array[i] + '\n'
    
    print(names_string)


    num = validate_file_names_to_array_number(len(names_array))
    num = num -1

    file_name = names_array[num]

    print('This is the file you chose: ', file_name)
    return file_name



def validate_file_names_to_array_number(array_length):
    while True:
        try:
            num = int(input('Please enter the number of the file you want to use: '))
            if num < 1 or num > array_length:
                print('Please enter a valid number.')
                continue
            else:
                return num
        except:
            print('This is not a valid number.')



#Use of variable __name__  
if __name__=="__main__": 
    main()

    
