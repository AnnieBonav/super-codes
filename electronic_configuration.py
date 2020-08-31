
"""
Ana Boavides Aguilar
Electronic Configuration.
14 August 2020
"""
import math
atomic_number = int(input('Please enter your atomic number: '))

#I declare my 2 variables, an i (initializer) and a matrix
elect_config_matrix = [[2,2,6,2,6,2,10,6,2,10,6,2,14,10,6,2,14,10,6], ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '6f', '5d', '6p', '7s', '7f', '6d', '7p'], [1, 3, 5, 7], [-1, 0, 1], [-2,-1,0,1,2], [-3,-2,-1,0,1,2,3]]

print('\n' + 'HERE IS YOUR ATOM´S INFORMATION' + '\n' + 'Atomic number = ', atomic_number)

def electronic_configuration(atomic_number):
    i = 0
    my_ElectConfig = []
    while atomic_number > 0:
        #We substract the array electrons from the atomic number
        atomic_number = atomic_number - elect_config_matrix[0][i]

        #If the atomic number becomes lower than 0, then that substraction becomes positive and we attach it as the last part of the congiguration
        if atomic_number < 0:
            atomic_number = atomic_number + elect_config_matrix[0][i]
            my_ElectConfig.append((elect_config_matrix[1][i]) + '^' + str(atomic_number))
            # The only reazon I substract it up again is so the loop stops, if not the while would continue.
            atomic_number = atomic_number - elect_config_matrix[0][i]
        #If the atomic number is greater than 0, then the normal substraction continues

        else:
            #We add the strings to the elecric configuration
            my_ElectConfig.append((elect_config_matrix[1][i]) + '^' + str(elect_config_matrix[0][i]))
        
        # i sum 1 to my initializer
        i = i +1
    return my_ElectConfig

my_ElectConfig = electronic_configuration(atomic_number)

def my_ValenceFtBlock(my_ElectConfig):
    if len(my_ElectConfig[-1]) == 4:
        #Valence number
        valence_number = my_ElectConfig[-1][-1]
        #Block letter
        block_letter = my_ElectConfig[-1][-3]
    else:
        valence_number = my_ElectConfig[-1][-2] + my_ElectConfig[-1][-1]
        #Block letter
        block_letter = my_ElectConfig[-1][-4]

    return valence_number, block_letter

valence_number = int(my_ValenceFtBlock(my_ElectConfig)[0])
print('This is your valence number: ', valence_number)
block_letter = my_ValenceFtBlock(my_ElectConfig)[1]
print('This is your block: ' + block_letter + '\n')

print('HERE ARE YOUR QUANTUM NUMBERS')
def my_quantumNumbers(valence_number, numSpin):
    if block_letter == 's' or block_letter == 'p':

        print('You have ', math.floor(math.fabs(valence_number-8)), ' electrons to use.')
        if block_letter == 's':
            print('Your m = 0')
            if valence_number <= elect_config_matrix[2][numSpin]:
                print('Your spin is +1/2')
            else:
                print('Your spin is -1/2')
        else:
            print('Your m =', elect_config_matrix[3][numSpin])
            if valence_number <= elect_config_matrix[2][numSpin]:
                print('Your spin is +1/2')
            else:
                print('Your spin is -1/2')


    elif block_letter == 'd':
        print('I am sorry, I don´t know how many electrones you can use.')
        if valence_number <= elect_config_matrix[2][numSpin]:
            print('Your spin = +1/2')
        else:
            print('Your spin = -1/2')


    else:
        if valence_number <= elect_config_matrix[2][numSpin]:
            print('Your spin = +1/2')
        else:
            print('Your spin = -1/2')
        print('I am sorry, I don´t know how many electrones you can use.')

def my_Spin(block_letter):
    if block_letter == 's':
        numSpin = 0
    elif block_letter == 'p':
        numSpin = 1
    elif block_letter == 'd':
        numSpin = 2
    else:
        numSpin = 3
    return numSpin

numSpin = my_Spin(block_letter)
my_quantumNumbers(valence_number, numSpin)

print('\n' + 'FINALLY, HERE IS YOUR ELECTRONIC CONFIGURATION:' + '\n' + str(my_ElectConfig) + '\n')
