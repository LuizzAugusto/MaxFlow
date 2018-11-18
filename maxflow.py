#! /usr/bin/env python3

# It's distributed under the MIT license (https://choosealicense.com/licenses/mit/)

import Input

def _main():
    Input.InstructionMethods.clear()
    
    while(Input.InstructionMethods.state['on']):
        Input.terminal()

if __name__ == '__main__':
    _main()