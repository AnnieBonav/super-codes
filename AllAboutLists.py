"""
All about strings and lists
Ana Bonavides
September 20, 2020

"""

def main():
    
    # This will be the lists that the user can fill out with my CRUD functions 
    bestiesList = []
    enemiesList = []
    
    # I define some filled lists to try the functions that need info on the lists to work.
    bestiesList = ['Ana', 'Bonavides', 'Aguilar', 'Besties']
    enemiesList = ['Ana', 'Bonavides', 'Aguilar', 'Enemies']
    
    cond = False
    print('Welcome to my program, here are the functions you can use' + '\n' + '1.0) Add a Person´s name' + '\n' + '2.0) Remove a Person´s name, knowing their name' + '\n' + '2.1) Remove a Person´s name, knowing their index in the Array' + '\n' + '3.0) See Lists' + '\n' '4.0) See the index from a Person´s Name' + '\n' + '4.1) Find index of a letter on String in an Array' + '\n' + '4.1) Count occurences of a String in a Name' + '\n' + '4.4) Find the occurences of a String in a hole array' + '\n' + '5.0) Reverse the list´s order' + '\n' + '5.1) Join different words with letter(s)' + '\n' + '0.0) Exit' + '\n')

    while cond == False:
        print('Please enter the number of the function you want to use: ')
        try:
            chooseFunc = float(input())
        except:
            print('Please enter a correct number.')
            continue
        
        # Calls the Create Function (Add a name to one of the lists.)
        if chooseFunc == 1.0:
            bestiesList, enemiesList = addPeople(bestiesList, enemiesList)
            print('\n' + 'These are your two lists after the addition: ' + '\n' + 'Besties List: ',bestiesList,'\n' + 'Enemies List: ',enemiesList,'\n')
            continue

        # Calls the delete function (Remove names to one if the lists, knowing it.)
        elif chooseFunc == 2.0:
            bestiesList, enemiesList = deletePeople(bestiesList, enemiesList)
            print('\n' + 'These are your two lists after the addition: ' + '\n' + 'Besties List: ',bestiesList,'\n' + 'Enemies List: ',enemiesList,'\n')
            continue

        # Pop
        elif chooseFunc == 2.1:
            bestiesList, enemiesList = popPeople(bestiesList, enemiesList)
            print('\n' + 'These are your two lists after the addition: ' + '\n' + 'Besties List: ',bestiesList,'\n' + 'Enemies List: ',enemiesList,'\n')
            continue

        # Read lists
        elif chooseFunc == 3.0:
            readPeople(bestiesList, enemiesList)
            continue
        
        # See index of a Person´s name
        elif chooseFunc == 4.0:
            indexPeople(bestiesList, enemiesList)
            continue

        elif chooseFunc == 4.1:
            findLetter(bestiesList)
            continue
        
        elif chooseFunc == 4.2:
            countLetters()
            continue

        elif chooseFunc == 4.3:
            countLettersList(bestiesList, enemiesList)
            continue

        # Revert the list
        elif chooseFunc == 5.0:
            revertList(bestiesList, enemiesList)

        # Join Strings
        elif chooseFunc == 5.1:
            joinedString = joinStrings()
            print('This is your joined string: ' + joinedString + '\n')
            continue

        # Exit
        elif chooseFunc == 0.0:
            print('Thank you for using my program!')
            cond = True

        else:
            print('That is not a function.')
            continue




# DEFINING MY FUNCTIONS

"""


VALIDATION STRINGS FUNCTIONS



"""

# This function is used to validate a given string (Capitalize and remove spaces)
def validateString():
    name = str.strip(input('Please enter the name: '))
    name = str.capitalize(name)
    print('This is the name you wrote: ' + name)
    return name



def validateCompleteName():
    name = str.strip(input('Please enter the name you want to remove: '))
    name = str.title(name)

    return name



# THis function is used to show how we can format things
def formatCompleteName():
    firstName = str.strip(input('Please enter the First Name: '))
    firstName = str.capitalize(firstName)

    lastName = str.strip(input('Please enter the Last Name: '))
    lastName = str.capitalize(lastName)

    completeName = f"{firstName} {lastName}"
    print('This is your complete Name: ' + completeName)
    return completeName



def continueValidate():
    while True:
        try:
            validChar = str(input('\n' + 'Please enter 1 if you would like to add another name, or 0 if you are done: '))
            if validChar == '0':
                return validChar
            elif validChar == '1':
                return validChar
            else:
                print('I am sorry, this is not one of the options.' + '\n')

        except:
            print('I am sorry, this is not a valid number.')




"""


VALIDATE NUMBERS FUNCTIONS



"""



# Validate number #0 or #1
# Option #
def validateNumber():
    while True:
        try:
            num = int(input())
            if num ==  0 or num ==1:
                return num
            else:
                print('This is not one of the options. \n ')
                continue
        except:
            print('Please enter a valid number')



def validateAnyInteger():
    while True:
        try:
            num = int(input('Please eneter 0 if you want to change the Besties List, or 1 if you want to change the Enemies List: '))
            return num
        except:
            print('Please enter a valid number.')



"""


CRUD FUNCTIONS



"""


# Add a Person in the chosen list 
# Option #1.0
def addPeople(bestiesList, enemiesList):
    print('Would you like to add besties or enemies?' + '\n' + 'Please eneter 0 if you want to change the Besties List, or 1 if you want to change the Enemies List: ')
    chooseList = validateNumber()

    print('Would you like to add a complete Name?' + '\n' + 'Please eneter 0 if you want to add a single Name, or 1 if you want to add a Complete name: ')
    completeName = validateNumber()
    validContinue = ''

    while True:
        if validContinue == '0':
            break
        
        else:
            if completeName == 1:
                personName = formatCompleteName()
            else:
                personName = validateString()

            if chooseList == 0:
                bestiesList.append(personName)
            else:
                enemiesList.append(personName)
        
            validContinue = continueValidate()
            print('Valid Char= ' + validContinue)
    
    return bestiesList, enemiesList



# Delete People in a given list
# Option #2.0
def deletePeople(bestiesList, enemiesList):
    print('Would you like to delete besties or enemies?')
    num = validateNumber()

    cond = False
    while cond == False:
        print('Please enter your Non-Bestie name, or 0 if you want to stop: ')
        nonBestie = validateCompleteName()
        try:
            if nonBestie == '0':
                cond = True
            else:
                if num == 0:
                    print('This is the name that will be deleted from the Besties List: '+ "'{}'".format(nonBestie))
                    # I remove the name from the list
                    bestiesList.remove(nonBestie)
                else:
                    print('This is the name that will be deleted from the Enemies List: '+ "'{}'".format(nonBestie))
                    # I remove the name from the list
                    enemiesList.remove(nonBestie)

        except:
            print('I am sorry, but this is not a valid name. Please check your spelling.' + '\n')
            continue
    
    return bestiesList,enemiesList



# Pop people from a given list
# Option #2.1
def popPeople(bestiesList, enemiesList):
    print('Would you like to pop besties or enemies?')
    num = validateNumber()

    cond = False
    while cond == False:
        personIndex = input('Please enter the Index of the Person you want to remove, or "s" if you want to stop: ')
        try:
            if personIndex == 's':
                cond = True
            else:
                if num == 0:
                    print('This is the name that will be deleted from the Besties List: ' + bestiesList[int(personIndex)])
                    # I remove the name from the list taking account the index
                    continue
                else:
                    print('This is the name that will be deleted from the Enemies List: ' + enemiesList[int(personIndex)])
                    # I remove the name from the list taking account the index
                    continue
        except:
            print('I am sorry, but this is not a valid index.' + '\n')
            continue

    return bestiesList,enemiesList



# Read given list 
# Option #3.0
def readPeople(bestiesList, enemiesList):
    print('Would you like to read the besties or enemies list?')
    chooseList = validateNumber()

    # printing the list using * operator separated
    if chooseList == 0:
        print('This is your besties list: ')
        print(*bestiesList, sep = ', ')
    else:
        print('This is your enemies list: ')
        print(', '.join(enemiesList))



"""


FIND THINGS FUNCTIONS



"""

# Get the index from a name
# Option #4.0
def indexPeople(bestiesList, enemiesList):
    print('Would you like to add besties or enemies?')
    num = validateNumber()
    
    cond = False
    while cond == False:
        print('Please enter the name of the person you want to get the index from, or "e" if you want to exit: ')
        nameCheck = validateString()

        try:
            if nameCheck == 'E':
                cond = True            
            else:
                if num == 0:
                    index = bestiesList.index(nameCheck)
                else:
                    index = enemiesList.index(nameCheck)
                print(index)
        except:
            print('Please enter a valid name.' + '\n')





# Find Letter Index in String Function
# Option #4.1
def findLetter(bestiesList):
    cond = False
    while cond == False:
        try:
            bestieIndex = int(input('Please enter the index of the Name you want to check the letter in: '))
            bestieName = bestiesList[bestieIndex]
            cond = True
        except:
            print('Please enter a valid index number.')

    print('Name used: ' + bestieName + '\n')
    letter = str(input('Please enter the letter(s) you want to check first occurence index: '))
    letterIndex = bestieName.find(letter)
    print('Name: ' + bestieName + '\n' + 'Letter checked: ' + letter + '\n' + 'Index: ' + str(letterIndex) + '\n')




# Count Letter(s) in a String Function 
# Option #4.2
def countLetters():
    bestieName = str(input('Please enter the name you want to check: '))
    letter = str(input('Please enter the letter(s) you want to count: '))
    letterCount = bestieName.count(letter)
    print('Name: ' + bestieName + '\n' + 'Letter checked: ' + letter + '\n' + 'Ocurrences: ' + str(letterCount) + '\n')
    return letterCount



# Find the number of a string instance in a whole List
# Option #4.3
def countLettersList(bestiesList, enemiesList):
    print('Would you like to add besties or enemies?')
    num = validateNumber()
    counter = 0
    if num == 0:
        listLook = bestiesList
    else:
        listLook = enemiesList
    
    cond = False
    while cond == False:
        stringLooked = str(input('Please enter the string you will look for in the List, or write 0 if you want to exit: '))
        if stringLooked == '0':
            cond = True
        else:
            for i in range(len(listLook)):
                counter = counter + listLook[i].count(stringLooked)
            print('\n' + 'String looked For: ' + stringLooked + '\n' + 'This is the count of the letter you chose, remember it is case-sensitive: ',counter,'\n')




"""


MODIFY LISTS FUNCTIONS



"""



# Revert the list´s order
# Option #3.2
def revertList(bestiesList, enemiesList):
    print('Would you like to reverse the besties or enemies list?')
    num = validateNumber()

    if num == 0:
        list.reverse(bestiesList)
        print(bestiesList, '\n')
    else:
        list.reverse(enemiesList)
        print(enemiesList, '\n')
    
    return bestiesList, enemiesList


# Join Strings Function 
# Option #5.0
def joinStrings():
    joiner = str(input('Please enter the joiner you want to use: '))
    print('Joiner' + joiner)

    i = 0
    wordsNum = 0
    completeList = []
    while i == 0:
        word = str(input('Please enter the word you want to add, or 0 if you don´t have any more words: '))
        if word == '0':
            i = i+1
        else:
            completeList.append(word)
            wordsNum = wordsNum +1

    joinedList = joiner.join(completeList)
    print('\n' + 'Number of words Added: ' + str(wordsNum) + '\n' + 'Joiner: ' + joiner + '\n' + 'This is your complete list: ', completeList)
    
    return joinedList
    # http://pythontutor.com/visualize.html#code=def%20joinStrings%28%29%3A%0A%20%20%20%20joiner%20%3D%20str%28input%28'Please%20enter%20the%20joiner%20you%20want%20to%20use%3A%20'%29%29%0A%20%20%20%20joiner%20%3D%20'%22'%20%2B%20joiner%20%2B%20'%22'%0A%0A%20%20%20%20i%20%3D%200%0A%20%20%20%20wordsNum%20%3D%200%0A%20%20%20%20completeString%20%3D%20''%0A%20%20%20%20while%20i%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20word%20%3D%20str%28input%28'Please%20enter%20the%20word%20you%20want%20to%20add,%20or%200%20if%20you%20don%C2%B4t%20have%20any%20more%20words%3A%20'%29%29%0A%20%20%20%20%20%20%20%20print%28'This%20is%20your%20word%3A%20'%20%2B%20word%29%0A%20%20%20%20%20%20%20%20if%20word%20%3D%3D%20'0'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%3D%20i%2B1%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20wordsNum%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20completeString%20%3D%20'%22'%20%2B%20word%20%2B%20'%22'%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20wordsNum%20%3D%20wordsNum%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20completeString%20%3D%20','%2B%20'%22'%20%2B%20word%20%2B%20'%22'%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20wordsNum%20%3D%20wordsNum%20%2B1%0A%0A%20%20%20%20completeString%20%3D%20'%28'%20%2B%20completeString%20%2B%20'%29'%0A%20%20%20%20joinedString%20%3D%20joiner.join%28completeString%29%0A%0A%20%20%20%20print%28'Number%20of%20words%20Added%3A%20'%20%2B%20str%28wordsNum%29%20%2B%20'%5Cn'%20%2B%20'Joiner%3A%20'%20%2B%20joiner%20%2B%20'%5Cn'%29%0A%20%20%20%20return%20joinedString%0A%20%20%20%20%0A%0AjoinStrings%28%29&cumulative=false&curInstr=22&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%22-%22,%22Annie%22,%22Cesar%22%5D&textReferences=false




if __name__=="__main__": 
    main()
