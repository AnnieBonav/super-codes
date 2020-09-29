"""
Annie Bonavides ft Tony ft George
ordenar listas de menor a mayor
"""

print('You can use this code to add the number of arrays you want and sort them out')

def addNumbersArray():
    array = []
    while True:
        try:
            value = input('Please enter a number, or * if you want to stop: ')
            if value == '*':
                print('You have completed your list.\n')
                return array
            else:
                value = int(value)
                array.append(value)
        except:
            print('Are you sure you can read?')


def main():
    
    array1 = addNumbersArray()
    array2 = addNumbersArray()
    print(array1, array2, sep = '\n', end = '\n')

    """
    array1 = [0,0,0,1,13,14,3,2,4,0,9,1,2,0,2,1,2,1,3,4,5,5]
    array2 = [9,8,8,7,6,5,4,40,0,4,0,5,2,4,8,6,9,0,8,4,9,5,7,2,3,0,7,8,2]
    """
    myArray = array1 + array2

    ordenarNum(myArray)


def ordenarNum(myArray):
    print('This is my joined array:',myArray, sep='\n', end = '\n')
    sortedArray = []
    # For that iterates 'n'
    #  times where n = the length of the array
    
    # I start my master for
    for i in range(len(myArray)):
        counterK = 0
        if i == 0:
            sortedArray.append(myArray[i])
            i += 1
            continue
        
        for k, element1 in enumerate(sortedArray, 0):

            if myArray[i] > element1:
                addNumberK = myArray[i]
                counterK +=1

                # If the length of the sorted Array is equal to my numerator k (plus one, because I want to include all alements)
                # Then it means that the element in myArray[i] is the last one (the biggest so far) so I just need to append it.
                if k+1 == len(sortedArray):
                    # I append addNumberK (which is the biggest number so far) to my sortedArray
                    sortedArray.append(addNumberK)
                    # I break the cycle because I already appended the myArray[i] element if this for loop (the for k, element1 in enumerate(sortedArray, 0))
                    # What will happen next is that my master For gets executed again, so I will be evaluating my next number (the next myArray[i])
                    break
                
                # If the length of the sorted Array is not equal to the numerator, then it means that myArray[i] 
                # hasn´t been evaluated (as bigger or smaller) than all the numbers in the sortedArray
                continue

            else:
                # If myArray[i] element is smaller or equal than the element, then it will be appended in counterK index
                sortedArray.insert(counterK, myArray[i])
                break 
        i += 1

    print('\nThis is your sorted Array:',sortedArray, sep = '\n', end = '\n')


#Use of variable __name__  
if __name__=="__main__": 
    main()
