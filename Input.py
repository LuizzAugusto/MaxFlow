# It's distributed under the MIT license (https://choosealicense.com/licenses/mit/)

import InstructionMethods

try:
    import readline
except:
    pass

instructionSet = InstructionMethods.instructionSet

def terminal():
    if(instructionSet == {}):
        print('Define Input.instructionSet dict first.')
        exit(1)

    instruction = input('> ').split(' ')

    try:
        execute(instruction)
    except KeyError:
        print("Instruction not found.")

def execute(instruction):
    instructionSet[instruction[0]](*instruction)